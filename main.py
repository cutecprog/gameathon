"""Hold game code in this file"""

from lib.display import hbar, GraphicVar

def main():
        from time import sleep
        pressure_valve = GraphicVar((1, 80), hbar,  32, 4)
        pressure_valve2 = GraphicVar((2, 80), hbar,  32, 0)
        pressure_valve.show()
        pressure_valve2.show()
        for i in range(0,256):
                pressure_valve.value = i
                pressure_valve2.value = i
                sleep(.04)
        sleep(1)
        pressure_valve.hide()
        pressure_valve2.hide()

if __name__=='__main__':
        main() 
