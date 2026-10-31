# Imports go at the top
from microbit import *
import music

set_volume(50)

# Code in a 'while True:' loop repeats forever
while True:
    light=display.read_light_level()
    
    if light<=120:
        display.show(Image.SAD)
        music.play(music.JUMP_DOWN)
    
    else:
        display.show(Image.HAPPY)
       
    sleep(1000)

        