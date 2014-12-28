"""Hold game code in this file"""

from lib.keyboard import getch, Cursor, Key, loc

def main():
        a = Cursor([20,80], 'u')
        last_position = list(a.position)
        while True:
                ch = getch()
                if ch == Key.LEFT_ARROW:
                        last_position = list(a.position)
                        a.position[1] -= 1
                elif ch == Key.RIGHT_ARROW:
                        last_position = list(a.position)
                        a.position[1] += 1
                elif ch == Key.UP_ARROW:
                        last_position = list(a.position)
                        a.position[0] -= 1
                elif ch == Key.DOWN_ARROW:
                        last_position = list(a.position)
                        a.position[0] += 1
                elif ch == 'q':
                        break
                print loc(last_position) + 'o'
                print a

if __name__=='__main__':
        main()
