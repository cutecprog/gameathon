"""Hold game code in this file"""

from lib.keyboard import getch, Key, Cursor
from lib.display import loc
from sys import stdout
from os import system

def main():
        system('setterm -cursor off')
        system('clear')
        print Key.H_WORM + Key.BL_WORM + Key.BR_WORM
        print loc(20,20) + '\033[7m  \033[0m'
        me = LiveCell([80,80])
        print me
        while True:
                ch = getch()
                print loc(1, 80) + repr(ch) + ' '*13
                if Key.UP_ARROW in ch:
                        me.move_up()
                if Key.DOWN_ARROW in ch:
                        me.move_down()
                if Key.LEFT_ARROW in ch:
                        me.move_left()
                if Key.RIGHT_ARROW in ch:
                        me.move_right()
                if ' ' in ch:
                        me.hp -= 1
                elif ch == 'q':
                        break
                print me
        system('clear')
        system('setterm -cursor on')

class LiveCell(object):
        MAX_HP = 8
        def __init__(self, pos = [0,0]):
                self.pos = pos
                self.hp  = self.MAX_HP
                y, x = self.pos
                if y%2 == 0:
                        self.sym = Key.T_SQUARE
                else:
                        self.sym = Key.B_SQUARE
        def __repr__(self):
                y, x = self.pos
                return self._show_hp() + '\033[%s;%sH' % (str(y/2), str(x)) + self.sym
        def _show_hp(self):
                hp_bar = '\033[1;1H'
                for n in range(0, self.hp):
                        hp_bar += Key.HEART + ' '
                for n in range(self.hp, self.MAX_HP):
                        hp_bar += Key.EMPTY_HEART + ' '
                return hp_bar
        def move_up(self):
                y, x = self.pos
                if y%2:
                        self.sym = Key.T_SQUARE
                        self.pos[0] -= 1
                else:
                        stdout.write(loc(y/2, x) + ' ')
                        self.sym = Key.B_SQUARE
                        self.pos[0] -= 1
        def move_down(self):
                y, x = self.pos
                if y%2 == 0:
                        self.sym = Key.B_SQUARE
                        self.pos[0] += 1
                else:
                        stdout.write(loc(y/2, x) + ' ')
                        self.sym = Key.T_SQUARE
                        self.pos[0] += 1
        def move_left(self):
                y, x = self.pos
                stdout.write(loc(y/2, x) + ' ')
                self.pos[1] -= 1
        def move_right(self):
                y, x = self.pos
                stdout.write(loc(y/2, x) + ' ')
                self.pos[1] += 1

if __name__=='__main__':
        main()
