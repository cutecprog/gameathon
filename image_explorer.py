from PIL import Image
from random import random
from lib.keyboard import getch
from lib.display import loc, GraphicVar
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
                for c in range(-(2*view), (2*view)+1):
                        if c==0 and r ==0:
                                print '\033[41;96m'
                        print loc(16+r,30+c) + foo(pix[x+c,y+r])
                        print '\033[0m'        

def display_loop(pix, pos, view):
        while pos != [0,0]:
                print_pixels(pix, pos, view)

def explore(im, view):
        ch = ''
        pix = im.load()
        x_max, y_max = im.size
        pos = [20,20]
        key_binds = {'\x1b[D': (0, -1), '\x1b[A': (-1, 0),                    \
                     '\x1b[C': (0, 1), '\x1b[B': (1,0)}
        display_thread = Thread(target=display_loop, args=[pix,pos,view])
        display_thread.start()
        while ch != 'q':
                ch=getch()
                if ch in key_binds:
                        x, y = pos
                        y_offset, x_offset = key_binds[ch]
                        x = saturate(x+x_offset, x_max-view, view)
                        y = saturate(y+y_offset, y_max-view, view)
                        pos[0] = x
                        pos[1] = y
                #print_pixels(pix, pos, view)
        pos[0] = 0
        pos[1] = 0

im = Image.open('../tl1.png')
system('clear')
explore(im, 8)
system('clear')
