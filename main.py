def main():
        from time import sleep
        for i in range(0,256):
                print '\033[1;80H'+horizontal_bar(i)
                sleep(.01)

def horizontal_bar(length):
        """Return horizontal_bar the size of length in 1/8 of a column.

        """
        bar =  '\xe2\x96\x88'*(length/8)
        bar += '\xe2\x96' + chr(0x8f - length%8)
        return bar

if __name__=='__main__':
        main() 
