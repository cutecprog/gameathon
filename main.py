"""Hold game code in this file"""

from lib.display import loc, hbar, GraphicVar
from lib.keyboard import getch

def main():
        ch = ""
        pedal = GraphicVar((2,80), hbar, 32, 0)
        pedal.value = 128
        pedal.show()
        while ch != '\033':
                ch = getch()
                if ch[:2] == '\033[':
                        if ch[2] == 'D':   # Left Arrow
                                pedal.value = pedal.value/2.0
                        elif ch[2] == 'C': # Right Arrow
                                pedal.value = 3*pedal.value/2.0
                        elif ch[2] == 'A': # Up Arrow
                                pedal.value = 128
                msg = loc(5,80)
                print msg + ' '*8
                for c in ch:
                        msg += c + ' '
                print msg
                print pedal.value
        pedal.hide()

if __name__=='__main__':
        main() 
