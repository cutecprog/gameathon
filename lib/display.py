"""Hold generic shell display code in this file"""

def hbar(value):
        """Return horizontal bar the size of value in 1/8 of columns

        """
        bar =  '\xe2\x96\x88'*(value/8)
        bar += '\xe2\x96' + chr(0x8f - value%8)
        return bar

def loc(y,x):
        """Return string to move cursor to (y,x)

        """
        return '\033[%s;%sH' % (str(y),str(x))

def meter(illustrate, size, value):
        """Return printable visual representation of value

        """
        display  = illustrate(int(value))
        display += ' '*(size - len(display)/3)
        return display

def gaussed(size, sigma, value):
        """Deviate value with random.gauss function limit between 0 and size-1

        """
        from random import gauss
        return sorted([0, int(gauss(value, sigma)), size-1])[1]

class GraphicVar(object):
        def __init__(self, pos, illustrate, size, sigma = 0):
                from threading import Thread
                self.y              = pos[0]
                self.x              = pos[1]
                self.illustrate     = illustrate
                self.size           = size
                self.sigma          = sigma
                self.value          = 0
                self.display_thread = Thread(target=self.display_loop)
                self.displaying     = False
        def __repr__(self):
                """Return value with style at y,x

                """
                return loc(self.y, self.x) + meter(self.illustrate, self.size,\
                                                gaussed(self.size*8,          \
                                                self.sigma, self.value))
        def display_loop(self):
                """Print self continuously until program ends.

                """
                from time import sleep
                self.displaying = True
                while self.displaying:
                        print self
                        sleep(.083)
                print loc(self.y, self.x) + ' '*self.size
        def show(self):
                self.display_thread.start()
        def hide(self):
                self.displaying = False
        def bs_input(self):
                """Use arrow keys to set value with a binary search

                """
                from lib.keyboard import getch, Key
                self.value = 128
                start_value = self.value
                n = start_value
                ch = ""
                while ch != '\r':
                        ch = getch()
                        if ch == Key.UP_ARROW:
                                self.value = start_value
                                n = start_value
                        elif ch == Key.LEFT_ARROW:
                                n /= 2
                                self.value -= n
                        elif ch == Key.RIGHT_ARROW:
                                n /= 2
                                self.value += n
