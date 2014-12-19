"""Hold game code in this file"""

def main():
        from os import system
        from lib.keyboard import getch, Key
        from random import randint
        from threading import Thread
        from lib.display import loc
        from string import whitespace
        system('setterm -cursor off')
        print "Press a key of a visable character you like"
        sym = ' '
        while sym[0] in whitespace or '\033' in sym:
                sym = getch()
        sym = sym[0]
        system('clear')
        add_player(sym)
        print loc(1,3) + "Press arrow key to select space"
        print loc(2,3) + "Press space to mark space"
        print loc(1, 38) + "Press ESC to clear board"
        print loc(2, 38) + "Press e to exit"
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
                elif ch == ' ' and is_turn(sym):
                        inserted = insert_data(pos, sym)
                        if inserted:
                                last_move = list(pos)
                                end_turn()
                elif ch == Key.ESC:
                        clear_data()
        remove_player(sym)
        system('setterm -cursor on')
        system("clear")

def add_player(sym):
        with open('turn.data', 'r+') as f:
                players = f.read().strip('\n')
                players = sym + players
                f.seek(0)
                f.write(players)
                f.truncate()

def remove_player(sym):
        with open('turn.data', 'r+') as f:
                players = list(f.read())
                remaining_players = []
                for player in players:
                        if player != sym:
                                remaining_players.append(player)
                players = ''.join(remaining_players)
                f.seek(0)
                f.write(players)
                f.truncate()

def is_turn(sym):
        current_player = ''
        with open('turn.data', 'r') as f:
                current_player = f.read(1)
        if sym == current_player:
                return True
        return False

def end_turn():
        with open('turn.data', 'r+') as f:
                players = f.read()
                players = players[1:] + players[0]
                f.seek(0)
                f.write(players)
                f.truncate()

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
                else:
                        return
                data = ''.join(data)
                f.seek(0)
                f.write(data)
                f.truncate()
        return True

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
