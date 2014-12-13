"""Hold generic shell keyboard reading code in this file"""

def getch():
        """Get one to four characters press at once and return them

        """
        import tty, termios
        from os import read
        from sys import stdin
        fd = stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
                tty.setraw(fd)
                ch = read(fd, 4)
        finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
