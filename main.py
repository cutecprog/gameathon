from lib.display import meter, gaussed

def main():
        from time import sleep
        for i in range(0,64):
                print meter((1,80), 32, gaussed(256, 4, (i/3)*12))
                sleep(.083)

if __name__=='__main__':
        main() 
