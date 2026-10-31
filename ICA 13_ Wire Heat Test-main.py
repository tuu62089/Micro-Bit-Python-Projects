# Imports go at the top
from microbit import *

# on start
display.show("?")

# Code in a 'while True:' loop repeats forever
while True:
    if button_a.was_pressed():
        # on button A pressed
        display.show(1)
        pin0.write_digital(1)

    if button_b.was_pressed():
        # on button B pressed
        display.show(0)
        pin0.write_digital(0)
