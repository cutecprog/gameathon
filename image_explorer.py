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

def print_pixels(pix, pos, view):
        print loc(1, 80), pos, ' '*8
        x, y = pos
        for r in range(-view, view+1):
                for c in range(-view, view+1):
                        if c==0 and r ==0:
                                print '\033[41;96m'
                        print loc(38+r,136+c*2) + foo(pix[x+c,y+r])
                        print '\033[0m'        

def display_loop(pix, pos, view):
        while pos != [0,0]:
                print_pixels(pix, pos, view)

def explore(im, view):
        from sys import stdin
        from termios import tcgetattr, tcsetattr, TCSADRAIN
        from tty import setraw
        from os import read
        fd = stdin.fileno()
        old_settings = tcgetattr(fd)
        setraw(fd)
        system('setterm -cursor off')

        ch = ''
        pix = im.load()
        x_max, y_max = im.size
        pos = [view,view]
        key_binds = {Key.LEFT_ARROW: (0, -1), Key.UP_ARROW: (-1, 0),          \
                     Key.RIGHT_ARROW: (0, 1), Key.DOWN_ARROW: (1,0),          \
                     read(fd,1): (-view,0),                                   \
                     read(fd,1): (0, -view),                                  \
                     read(fd,1): (view,0),                                    \
                     read(fd,1): (0, view)}
        display_thread = Thread(target=display_loop, args=[pix,pos,view])
        display_thread.start()
        while ch != 'q':
                ch = read(fd, 4)
                if ch in key_binds:
                        x, y = pos
                        y_offset, x_offset = key_binds[ch]
                        x = saturate(x+x_offset, x_max-view, view)
                        y = saturate(y+y_offset, y_max-view, view)
                        pos[0] = x
                        pos[1] = y
        pos[0] = 0
        pos[1] = 0
        tcsetattr(fd, TCSADRAIN, old_settings)
        system('setterm -cursor on')

im = Image.open('../tl1.png')
system('clear')
explore(im, 32)
system('clear')
