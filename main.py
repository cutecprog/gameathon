"""Hold game code in this file"""

from lib.keyboard import getch, Cursor

def main():
        print getch()
        a = Cursor([4,0], '<')
        print a.position
        print a.symbol

if __name__=='__main__':
        main()
