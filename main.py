"""Hold game code in this file"""

from lib.display import loc
from lib.keyboard import getch

def main():
        ch = ""
        while ch != '\033':
                ch = getch()
                msg = loc(5,80)
                print msg + ' '*8
                for c in ch:
                        msg += c + ' '
                print msg

if __name__=='__main__':
        main() 
