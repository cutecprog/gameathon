"""Hold game code in this file"""

from lib.display import loc, hbar, GraphicVar
from lib.keyboard import getch

def main():
        ch = ""
        pedal = GraphicVar((2,80), hbar, 32, 0)
        pedal.value = 128
        pedal.show()
        start_value = pedal.value
        num_left  = 0
        num_right = 0
        while ch != '\033':
                ch = getch()
                if ch[:2] == '\033[':
                        if ch[2] == 'D':   # Left Arrow
                                num_left += 1
                        elif ch[2] == 'C': # Right Arrow
                                num_right += 1
                        elif ch[2] == 'A': # Up Arrow
                                pedal.value = start_value
                                num_left = 0
                                num_right = 0
                msg = loc(5,80)
                print msg + ' '*3
                print msg + str(int(pedal.value))
                
        pedal.hide()

if __name__=='__main__':
        main() 
