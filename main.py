"""Hold game code in this file"""

def main():
        from os import system
        from lib.keyboard import getch
        from random import randint
        system('clear')
        origin = (4,4)
        full_grid(origin)
        insert_data((2,2,2,2), 'A')
        print_data(origin)
        getch()

def print_data(origin):
        from sys import stdout
        data = ''
        with open('tmp.data','r') as f:
                data = f.read()
        for i in range(0, len(data)):
                w = (i/4)%4
                x = i%4
                y = (i/16)%4
                z = (i/64)%4 # Roll back to origin if i >= 256
                stdout.write(coord(origin, z,w,y,x) + data[i])

def insert_data(pos, sym):
        z, w, y, x = pos
        with open('tmp.data', 'r+') as f:
                data = list(f.read())
                data[x + 4*w + 16*y + 64*z] = sym
                data = ''.join(data)
                f.write(data)
                #print data

def coord(origin, z, w, y, x):
        """Convert 4d coordinates to a position in the shell screen.

        """
        from lib.display import loc
        return loc(origin[0] + 2*y + 8*z, origin[1] + 4*x + 15*w)

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
        grid(y,    x); grid(y,    x+15); grid(y,    x+30); grid(y,    x+45)
        grid(y+8,  x); grid(y+8,  x+15); grid(y+8,  x+30); grid(y+8,  x+45)
        grid(y+16, x); grid(y+16, x+15); grid(y+16, x+30); grid(y+16, x+45)
        grid(y+24, x); grid(y+24, x+15); grid(y+24, x+30); grid(y+24, x+45)

if __name__=='__main__':
        main()
