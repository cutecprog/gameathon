"""Hold game code in this file"""

from lib.display import loc, hbar, GraphicVar
from lib.keyboard import getch

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
        pedal.bs_input()
        gauge.sigma = 0
        if pedal.value == gauge.value:
                print 'You win'
                pedal.hide()
                gauge.hide()
                return
        else:
                print 'You loss by', pedal.value - gauge.value
        getch()
        pedal.hide()
        gauge.hide()
        main()

if __name__=='__main__':
        main() 
