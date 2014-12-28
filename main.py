"""Hold game code in this file"""

from lib.keyboard import getch, Cursor, Key

def main():
        print getch()
        a = Cursor([20,80], '<')
        print a.position
        print a.symbol
        print a
        while True:
                ch = getch()
                if ch == Key.LEFT_ARROW:
                        a.position[1] -= 1
                elif ch == Key.RIGHT_ARROW:
                        a.position[1] += 1
                elif ch == Key.UP_ARROW:
                        a.position[0] -= 1
                elif ch == Key.DOWN_ARROW:
                        a.position[0] += 1
                if ch[0] == Key.ESC:
                        print ch[1:]
                elif ch == 'q':
                        break
                print a

if __name__=='__main__':
        main()
