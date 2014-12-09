def main():
        from time import sleep
        from random import gauss
        for i in range(0,64):
                print meter((1,80), 32, sorted([0,int(gauss(128,16)),256])[1])
                sleep(.083)

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

def meter(pos, size, value):
        """Return printable visual representation of value

        """
        display  = horizontal_bar(value)
        display += ' '*(size - len(display)/3)
        display  = loc(pos[0], pos[1]) + display
        return display

if __name__=='__main__':
        main() 
