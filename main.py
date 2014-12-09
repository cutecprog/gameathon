from lib.display import meter, gaussed, loc, hbar, GraphicVar

def main():
        from time import sleep
        for i in range(0,64):
                print loc(1,80) + meter(hbar, 32, gaussed(256, 4, (i/3)*12))
                sleep(.083)
        wind_speed = GraphicVar((20, 80), 512, 4)

if __name__=='__main__':
        main() 
