import music
from microbit import *

#on start
destroyed=False
start_time = running_time()

# Code in a 'while True:' loop repeats forever
while True:
    tempf = temperature()*1.8+32
    
    if destroyed == True:
        display.scroll('Destroyed', delay= 55)    
        music.play(music.FUNERAL)

    elif tempf >= 85 and tempf <= 88:
        pin0.write_digital(0)
        display.scroll('Ok', delay= 80)
        start_time = running_time()

    else:
        display.scroll("Out of Range", delay= 55)

        if tempf < 85:
            pin0.write_digital(1)

        else:
            pin0.write_digital(0)

        if (running_time() - start_time)>20000:
            destroyed = True

    sleep(1)