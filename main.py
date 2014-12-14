"""Hold game code in this file"""

from lib.display import loc, hbar, GraphicVar
from lib.keyboard import getch

def main():
        from random import randint
        from os import system
        from time import sleep
        system('setterm -cursor off')
        system('clear')
        score = 0
        hp = GraphicVar((1,80), hbar, 8)
        hp.value = 64
        hp.show()
        while hp.value > 0:
                print loc(1, 100) + "Score " + str(score)
                pedal = GraphicVar((3,80), hbar, 32)
                gauge = GraphicVar((2,80), hbar, 32, 4)
                gauge.value = randint(0,255)
                pedal.show()
                gauge.show()
                pedal.bs_input()
                gauge.sigma = 0
                loss = (gauge.value - pedal.value)**2
                score += 16 - loss
                hp.value -= loss
                #getch()
                pedal.hide()
                gauge.hide()
        hp.hide()
        system('clear')
        system('setterm -cursor on')
        print "Final score:", score

if __name__=='__main__':
        main() 
