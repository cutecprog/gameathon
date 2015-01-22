from PIL import Image
from random import random
from lib.display import loc, GraphicVar
from lib.keyboard import Key
from os import system
from threading import Thread

def dither(x):
        n = int(x)
        if x-n > random():
                n += 1
        return n

def bar(n):
        if n:
                return '\xe2\x96' + chr(128+n)
        return ' '

def foo(n):
        return bar(8 - dither(n/32.))

def saturate(n, h, l=0):
        if n >= h:
                return h
        elif n < l:
                return l
        else:
                return n

def print_pixels(pix, pos):
        print loc(1, 80), pos, ' '*8
        x, y, view = pos
        for r in range(-view, view+1):
                for c in range(-view, view+1):
                        if c==0 and r ==0:
                                print '\033[41;96m'
                        print loc(38+r,136+c*2) + foo(pix[x+c,y+r])
                        print '\033[0m'        

def display_loop(pix, pos):
        while pos != [0,0,0]:
                try:
                        print_pixels(pix, pos)
                except:
                        pass

def explore(im, view):
        # init
        from sys import stdin
        from termios import tcgetattr, tcsetattr, TCSADRAIN
        from tty import setraw
        from os import read
        global locked
        fd = stdin.fileno()
        old_settings = tcgetattr(fd)
        setraw(fd)
        system('setterm -cursor off')
        # start
        ch = ''
        pix = im.load()
        x_max, y_max = im.size
        pos = [view,view,view]
        key_binds = {Key.LEFT_ARROW: (0, -1, 0), Key.UP_ARROW: (-1, 0, 0),    \
                     Key.RIGHT_ARROW: (0, 1, 0), Key.DOWN_ARROW: (1,0, 0),    \
                     read(fd,1): (-view, 0,     0),                           \
                     read(fd,1): (0,     -view, 0),                           \
                     read(fd,1): (view,  0,     0),                           \
                     read(fd,1): (0,     view,  0),                           \
                     '[': (0,0,-1), ']': (0,0,1)}
        display_thread = Thread(target=display_loop, args=[pix,pos])
        display_thread.start()
        while ch != 'q':
                ch = read(fd, 4)
                if ch in key_binds:
                        x, y, view = pos
                        y_offset, x_offset, view_offset = key_binds[ch]
                        x = saturate(x+x_offset, x_max-view, view)
                        y = saturate(y+y_offset, y_max-view, view)
                        view = saturate(view+view_offset, 32)
                        if view_offset:
                                system('clear')
                        pos[0] = x
                        pos[1] = y
                        pos[2] = view
        # end
        pos[0] = 0
        pos[1] = 0
        pos[2] = 0
        # clean up
        tcsetattr(fd, TCSADRAIN, old_settings)
        system('setterm -cursor on')

im = Image.open('../tl1.png')
system('clear')
explore(im, 4)
system('clear')
