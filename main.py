"""Hold game code in this file"""

from lib.keyboard import getch, Cursor

def main():
        print getch()
        a = Cursor([80,80], '<')
        print a.position
        print a.symbol
        print a

if __name__=='__main__':
        main()
