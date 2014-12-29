"""Hold game code in this file"""

from lib.keyboard import getch, Key, Cursor
from lib.display import loc
from sys import stdout
from os import system

def main():
        system('setterm -cursor off')
        system('clear')
        print loc(20,20) + '\033[7m  \033[0m'
        me = Player([80,80])
        print me
        while True:
                ch = getch()
                if ch == Key.UP_ARROW:
                        me.move_up()
                elif ch == Key.DOWN_ARROW:
                        me.move_down()
                elif ch == Key.LEFT_ARROW:
                        y,x = me.pos
                        stdout.write(loc(y/2,x) + ' ')
                        me.pos[1] -= 1
                elif ch == Key.RIGHT_ARROW:
                        y,x = me.pos
                        stdout.write(loc(y/2,x) + ' ')
                        me.pos[1] += 1
                elif ch == 'q':
                        break
                print me
        system('clear')
        system('setterm -cursor on')

class Player(object):
        def __init__(self, pos = [0,0]):
                self.pos = pos
                y, x = self.pos
                if y%2 == 0:
                        self.sym = Key.TV_WORM
                else:
                        self.sym = Key.BV_WORM
        def __repr__(self):
                y, x = self.pos
                if y%2 == 0:
                        return '\033[%s;%sH' % (str(y/2), str(x)) + Key.TV_WORM
                else:
                        return '\033[%s;%sH' % (str(y/2), str(x)) + Key.BV_WORM
        def move_up(self):
                y, x = self.pos
                if self.sym == Key.BV_WORM:
                        self.sym = Key.TV_WORM
                        self.pos[0] -= 1
                elif self.sym == Key.TV_WORM:
                        stdout.write(loc(y/2, x) + ' ')
                        self.sym = Key.BV_WORM
                        self.pos[0] -= 1
                elif y%2 == 0: # Top
                        self.sym = Key.TV_WORM
                else:          # Bottom
                        self.sym = Key.BV_WORM
        def move_down(self):
                y, x = self.pos
                if self.sym == Key.BV_WORM:
                        stdout.write(loc(y/2, x) + ' ')
                        self.sym = Key.TV_WORM
                        self.pos[0] += 1
                elif self.sym == Key.TV_WORM:
                        self.sym = Key.BV_WORM
                        self.pos[0] += 1
                elif y%2 == 0: # Top
                        self.sym = Key.TV_WORM
                else:          # Bottom
                        self.sym = Key.BV_WORM
        #def move_left(self):
        #        if self.sym == K.BV_WORM

if __name__=='__main__':
        main()
