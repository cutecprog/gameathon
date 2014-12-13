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
