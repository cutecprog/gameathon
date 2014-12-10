from lib.display import hbar, GraphicVar, display_loop

def main():
        from time import sleep
        wind_speed = GraphicVar((1, 80), hbar,  32, 4)
        display_loop(wind_speed)
        for i in range(0,240):
                wind_speed.value = i
                sleep(.01)
        sleep(1)

if __name__=='__main__':
        main() 
