# Imports go at the top
from microbit import *

counter=0
destroy=False

# Code in a 'while True:' loop repeats forever
while True:

    if destroy == True:
        display.show(Image.NO)
        sleep (1000)

    elif display.read_light_level()<25:
        counter=counter+1
        display.show(Image.SAD)
        sleep(1000)

        if counter >=10:
            destroy=True

    else:
        counter=0
        display.show(Image.YES)
        sleep(1000)

        