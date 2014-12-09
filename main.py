from lib.display import meter, gaussed, loc

def main():
        from time import sleep
        for i in range(0,64):
                print loc(1,80) + meter(32, gaussed(256, 4, (i/3)*12))
                sleep(.083)

if __name__=='__main__':
        main() 
