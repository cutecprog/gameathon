from lib.display import hbar, GraphicVar, display_loop

def main():
        from time import sleep
        wind_speed = GraphicVar((1, 80), hbar,  32, 4)
        for i in range(0,64):
                wind_speed.value = (i/3)*12
                print wind_speed
                sleep(.083)
        display_loop(wind_speed)
        sleep(1)

if __name__=='__main__':
        main() 
