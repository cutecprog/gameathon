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

def loc(pos):
        """Return string to move cursor to pos

        """
        y, x = pos
        return '\033[%s;%sH' % (str(y),str(x))

class Key:
        """Hold special characters

        """
        UP_ARROW = '\033[A'
        DOWN_ARROW = '\033[B'
        RIGHT_ARROW = '\033[C'
        LEFT_ARROW = '\033[D'
        ESC = '\033'
        BACKSPACE = '\033[3~'
        HBAR = '\xe2\x94\x80'
        VBAR = '\xe2\x94\x82'
        TLBAR = '\xe2\x94\x8c'
        TRBAR = '\xe2\x94\x90'
        BLBAR = '\xe2\x94\x94'
        BRBAR = '\xe2\x94\x98'
class Cursor(object):
        """Hold a position one a terminal screen

        """
        def __init__(self, position, symbol):
                self.position = position
                self.symbol = symbol

        def __repr__(self):
                """Return printable string for symbol at position

                """
                return loc(self.position) + self.symbol
