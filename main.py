"""Hold game code in this file"""

from lib.display import hbar, GraphicVar

def main():
        from time import sleep
        wind_speed = GraphicVar((1, 80), hbar,  32, 4)
        wind_speed.display_loop()
        for i in range(0,256):
                wind_speed.value = i
                sleep(.04)

if __name__=='__main__':
        main() 
