"""Hold game code in this file"""

from lib.display import hbar, GraphicVar, meter, loc

def main():
        from time import sleep
        pressure_valve  = GraphicVar((1, 80), hbar,  32, 4)
        pressure_valve2 = GraphicVar((2, 80), hbar,  32, 0)
        pressure_valve.show()
        pressure_valve2.show()
        for i in range(0,264):
                pressure_valve.value  = i
                pressure_valve2.value = i
                print loc(3,80) + str((i/8)*8) + ' + ' + meter(hbar,1,i%8,)
                sleep(.04)
        raw_input()
        print loc(3,80) + "       "
        pressure_valve.hide()
        pressure_valve2.hide()

if __name__=='__main__':
        main() 
