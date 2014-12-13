"""Hold game code in this file"""

from lib.display import loc, hbar, GraphicVar
from lib.keyboard import getch, Key

def main():
        from random import randint
        from os import system
        system('clear')
        pedal = GraphicVar((2,80), hbar, 32)
        gauge = GraphicVar((1,80), hbar, 32, 4)
        pedal.value = 128
        gauge.value = randint(0,255)
        pedal.show()
        gauge.show()
        start_value = pedal.value
        n = start_value
        ch = ""
        while ch != '\r':
                ch = getch()
                if ch == Key.UP_ARROW:
                        pedal.value = start_value
                        n = start_value
                elif ch == Key.LEFT_ARROW:
                        n /= 2
                        pedal.value -= n
                elif ch == Key.RIGHT_ARROW:
                        n /= 2
                        pedal.value += n
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
