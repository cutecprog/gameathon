"""Hold generic shell keyboard reading code in this file"""

def getch():
        """Get one to four characters press at once and return them

        """
        from sys import stdin
        from termios import tcgetattr, tcsetattr, TCSADRAIN
        from tty import setraw
        from os import read
        fd = stdin.fileno()
        old_settings = tcgetattr(fd)
        try:
                setraw(fd)
                ch = read(fd, 4)
        finally:
                tcsetattr(fd, TCSADRAIN, old_settings)
        return ch

class Key:
        """Hold special characters

        """
        UP_ARROW = '\033[A'
        DOWN_ARROW = '\033[B'
        RIGHT_ARROW = '\033[C'
        LEFT_ARROW = '\033[D'
        ESC = '\033'
        BACKSPACE = '\033[3~'

class Cursor(object):
        """Hold a position one a terminal screen

        """
        def __init__(self, position, symbol):
                self.position = position
                self.symbol = symbol
