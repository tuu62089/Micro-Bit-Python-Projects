# Imports go at the top
from microbit import *
import music

# Code in a 'while True:' loop repeats forever
while True:
    light=display.read_light_level()
    
    if light<25:
        display.show(Image.SAD)
        music.play(music.JUMP_DOWN)

    elif light<=150:
        display.show(Image.YES)

    else:
        display.show(Image.NO)
        music.play(music.BA_DING)
       
    sleep(1000)

        