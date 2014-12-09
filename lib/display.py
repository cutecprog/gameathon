"""Hold generic shell display code in this file"""
def hbar(value):
        """Return horizontal bar the size of value in 1/8 of columns

        """
        bar =  '\xe2\x96\x88'*(length/8)
        bar += '\xe2\x96' + chr(0x8f - length%8)
        return bar

def loc(y,x):
        """Return string to move cursor to (y,x)

        """
        return '\033[%s;%sH' % (str(y),str(x))

def meter(illustrator, size, value):
        """Return printable visual representation of value

        """
        display  = illustrator(value)
        display += ' '*(size - len(display)/3)
        return display

def gaussed(size, sigma, value):
        """Deviate value with random.gauss function.

        """
        from random import gauss
        return sorted([0, int(gauss(value, sigma)), size-1])[1]

class graphic_var(object):
        def __init__(self, pos, size, sigma):
                self.y     = pos[0]
                self.x     = pos[1]
                self.size  = size
                self.sigma = sigma
                self.value = 0
