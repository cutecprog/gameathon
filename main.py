"""Hold game code in this file"""

from lib.display import loc, hbar, GraphicVar
from lib.keyboard import getch

def main():
        from random import randint
        from os import system
        system('clear')
        ch = ""
        pedal = GraphicVar((2,80), hbar, 32, 0)
        gauge = GraphicVar((1,80), hbar, 32, 4)
        pedal.value = 128
        gauge.value = randint(0,255)
        pedal.show()
        gauge.show()
        start_value = pedal.value
        n = start_value
        while ch != '\r':
                ch = getch()
                if ch[:2] == '\033[':
                        if ch[2] == 'D':   # Left Arrow
                                n /= 2
                                pedal.value -= n
                        elif ch[2] == 'C': # Right Arrow
                                n /= 2
                                pedal.value += n
                        elif ch[2] == 'A': # Up Arrow
                                pedal.value = start_value
                                n = start_value
        pedal.hide()
        gauge.hide()
        if pedal.value == gauge.value:
                print 'You win'
                return
        else:
                print 'You loss by', gauge.value - pedal.value
        getch()
        main()

if __name__=='__main__':
        main() 
