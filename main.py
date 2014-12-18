"""Hold game code in this file"""

def main():
        from os import system
        from lib.display import loc
        from lib.keyboard import getch
        system("clear")
        origin = (4,4)
        full_grid(origin)
        for i in range(0,4):
                print loc(origin[0]+2*i,origin[1]+4*i) + 'x'
                getch()

def grid(y,x):
        from lib.display import loc
        for i in range(0,7):
                if i%2 == 0:
                        print loc(y + i, x +  2) + '\xe2\x94\x82'
                        print loc(y + i, x +  6) + '\xe2\x94\x82'
                        print loc(y + i, x + 10) + '\xe2\x94\x82'
                else:
                        print loc(y + i, x +  2) + '\xe2\x94\xbc'
                        print loc(y + i, x +  6) + '\xe2\x94\xbc'
                        print loc(y + i, x + 10) + '\xe2\x94\xbc'
                        print loc(y + i, x     ) + '\xe2\x94\x80' * 2
                        print loc(y + i, x +  3) + '\xe2\x94\x80' * 3
                        print loc(y + i, x +  7) + '\xe2\x94\x80' * 3
                        print loc(y + i, x + 11) + '\xe2\x94\x80' * 2

def full_grid(pos):
        y,x = pos
        grid(y,    x); grid(y,    x + 15); grid(y,    x + 30); grid(y,    x+45)
        grid(y+8,  x); grid(y+8,  x + 15); grid(y+8,  x + 30); grid(y+8,  x+45)
        grid(y+16, x); grid(y+16, x + 15); grid(y+16, x + 30); grid(y+16, x+45)
        grid(y+24, x); grid(y+24, x + 15); grid(y+24, x + 30); grid(y+24, x+45)

if __name__=='__main__':
        main()
