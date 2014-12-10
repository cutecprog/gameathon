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
        display  = illustrate(value)
        display += ' '*(size - len(display)/3)
        return display

def gaussed(size, sigma, value):
        """Deviate value with random.gauss function.

        """
        from random import gauss
        return sorted([0, int(gauss(value, sigma)), size-1])[1]

class GraphicVar(object):
        def __init__(self, pos, size, sigma):
                self.y     = pos[0]
                self.x     = pos[1]
                self.size  = size
                self.sigma = sigma
                self.value = 0
        def get(self):
                return self.value
        def set(self, value):
                self.value = value

def display_loop(var):
        from threading import Thread
        Thread(target=_display_loop, args=vars).start()
def _display_loop(var):
        from sys import stdout
        while True:
                stdout.write(var)
