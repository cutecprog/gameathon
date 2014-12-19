"""Hold game code in this file"""

def main():
        from os import system
        from lib.keyboard import getch, Key
        from random import randint
        from threading import Thread
        system('setterm -cursor off')
        system('clear')
        sym = getch()
        origin = (4,4)
        full_grid(origin)
        pos = [0,0,0,0]
        last_move = []
        t = Thread(target=loop, args=[origin, pos])
        t.daemon = True
        t.start()
        ch = ''
        while ch != 'e':
                ch = getch()
                if ch == Key.UP_ARROW:
                        if pos[2] == 0:
                                pos[0] = (pos[0] - 1)%4
                                pos[2] = 3
                        else:
                                pos[2] -= 1
                elif ch == Key.DOWN_ARROW:
                        if pos[2] == 3:
                                pos[0] = (pos[0] + 1)%4
                                pos[2] = 0
                        else:
                                pos[2] += 1
                elif ch == Key.LEFT_ARROW:
                        if pos[3] == 0:
                                pos[1] = (pos[1] - 1)%4
                                pos[3] = 3
                        else:
                                pos[3] -= 1
                elif ch == Key.RIGHT_ARROW:
                        if pos[3] == 3:
                                pos[1] = (pos[1] + 1)%4
                                pos[3] = 0
                        else:
                                pos[3] += 1
                elif ch == ' ':
                        insert_data(pos, sym)
                        last_move = list(pos)
                elif ch == 'u':
                        insert_data(last_move, ' ')
        clear_data()
        system('setterm -cursor on')
        system("clear")

def loop(origin, pos):
        from time import sleep
        while True:
                print_data(origin, pos)
                sleep(0.083)

def clear_data():
        with open('tmp.data', 'w') as f:
                f.seek(0)
                f.write(' '*256)
                f.truncate()

def print_data(origin, cursor):
        from sys import stdout
        data = ''
        with open('tmp.data','r') as f:
                data = f.read()
        for i in range(0, len(data)):
                w = (i/4)%4
                x = i%4
                y = (i/16)%4
                z = (i/64)%4 # Roll back to origin if i >= 256
                if cursor == [z, w, y, x]:
                        stdout.write(coord(origin, z,w,y,x) + '\033[7m'       \
                                         + data[i] + '\033[0m')
                else:
                        stdout.write(coord(origin, z,w,y,x) + data[i])

def insert_data(pos, sym):
        if len(pos) != 4:
                return
        z, w, y, x = pos
        with open('tmp.data', 'r+') as f:
                data = list(f.read())
                index = x + 4*w + 16*y + 64*z
                if data[index] == ' ' or sym == ' ':
                        data[index] = sym
                data = ''.join(data)
                f.seek(0)
                f.write(data)
                f.truncate()

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
