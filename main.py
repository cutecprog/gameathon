def main():
        for i in range(0,17):
                print horizontal_bar(i)

def horizontal_bar(length):
        """Return horizontal_bar the size of length in 1/8 of a column.

        """
        bar =  '\xe2\x96\x88'*(length/8)
        if length%8:
                bar += ','
        return bar

if __name__=='__main__':
        main() 
