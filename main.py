"""Hold game code in this file"""

from lib.keyboard import getch, Key, Cursor

def main():
        from lib.display import loc
        from sys import stdout
        from os import system
        system('setterm -cursor off')
        system('clear')
        print loc(20,20) + '\033[7m  \033[0m'
        me = Player([80,80])
        print me
        while True:
                ch = getch()
                if ch == Key.UP_ARROW:
                        y,x = me.pos
                        if y%2==0:
                                stdout.write(loc(y/2,x) + ' ')
                        me.pos[0] -= 1
                elif ch == Key.DOWN_ARROW:
                        y,x = me.pos
                        if y%2:
                                stdout.write(loc(y/2,x) + ' ')
                        me.pos[0] += 1
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
        def __repr__(self):
                y, x = self.pos
                if y%2 == 0:
                        return '\033[%s;%sH' % (str(y/2), str(x)) + Key.TV_WORM
                else:
                        return '\033[%s;%sH' % (str(y/2), str(x)) + Key.BV_WORM

if __name__=='__main__':
        main()
