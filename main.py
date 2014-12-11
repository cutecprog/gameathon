"""Hold game code in this file"""

from lib.display import hbar, GraphicVar

def main():
        from time import sleep
        wind_speed = GraphicVar((1, 80), hbar,  32, 4)
        wind_speed.display_loop()
        #for i in range(0,256):
        #        wind_speed.value = i
        #        sleep(.04)
        if True:
                test = GraphicVar((5, 80), hbar,  32, 4)
                test.display_loop()
                sleep(1)
        test = GraphicVar((8, 80), hbar,  32, 4)
        test.display_loop()
        test.value = 64
        sleep(5)

if __name__=='__main__':
        main() 
