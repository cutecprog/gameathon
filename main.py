"""Hold game code in this file"""

from lib.display import loc, hbar, GraphicVar
from lib.keyboard import getch

def main():
        from random import randint
        from os import system
        system('clear')
        score = 0
        loss  = 0
        while loss < 144:
                print loc(1, 100) + "Score:", score
                pedal = GraphicVar((3,80), hbar, 32)
                gauge = GraphicVar((2,80), hbar, 32, 4)
                gauge.value = randint(0,255)
                pedal.show()
                gauge.show()
                pedal.bs_input()
                gauge.sigma = 0
                loss += (gauge.value - pedal.value)**2
                getch()
                pedal.hide()
                gauge.hide()
        system('clear')

if __name__=='__main__':
        main() 
