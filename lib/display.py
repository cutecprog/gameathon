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
        def __init__(self, pos, illustrate, size, sigma):
                self.y     = pos[0]
                self.x     = pos[1]
                self.size  = size
                self.sigma = sigma
                self.value = 0
                self.illustrate = illustrate
        def __repr__(self):
                """Return value with style at y,x

                """
                return loc(self.y, self.x) + meter(self.illustrate, self.size,\
                                                gaussed(self.size*8,          \
                                                self.sigma, self.value))
        def display_loop(self):
                """Print self continuously until program ends.

                """
                from threading import Thread
                t = Thread(target=self._display_loop)
                t.daemon = True
                t.start()
        def _display_loop(self):
                from time import sleep
                while True:
                        print self
                        sleep(.083)
