"""Hold game code in this file"""

from lib.keyboard import getch, Cursor

def main():
        print getch()
        a = Cursor(4)
        print a.position

if __name__=='__main__':
        main()
