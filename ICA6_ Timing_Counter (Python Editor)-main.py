from microbit import *

counter=0
destroyed=False

# Code in a 'while True:' loop repeats forever
while True:
    light_level=display.read_light_level()
    
    if destroyed:
        display.show(Image.NO)

    elif light_level<25:
        counter=counter+1
        display.show(Image.SAD)
        
        if counter>=10:
            destroyed=True
            display.show(Image.NO)

    elif light_level>=25:
        counter=0
        display.show(Image.YES)

    sleep(1000)
    
    