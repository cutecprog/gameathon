"""Hold generic shell display code in this file"""
def horizontal_bar(length):
        """Return horizontal_bar the size of length in 1/8 of a column

        """
        bar =  '\xe2\x96\x88'*(length/8)
        bar += '\xe2\x96' + chr(0x8f - length%8)
        return bar

def loc(y,x):
        """Return string to move cursor to (y,x)

        """
        return '\033[%s;%sH' % (str(y),str(x))

def meter(size, value):
        """Return printable visual representation of value

        """
        display  = horizontal_bar(value)
        display += ' '*(size - len(display)/3)
        return display

def gaussed(size, sigma, value):
        """Deviate value with random.gauss function.

        """
        from random import gauss
        return sorted([0, int(gauss(value, sigma)), size-1])[1]
