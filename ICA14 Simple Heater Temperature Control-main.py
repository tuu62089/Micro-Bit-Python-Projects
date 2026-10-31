# Imports go at the top
from microbit import *

counter=0
start = 0

# Code in a 'while True:' loop repeats forever
while True:
    temp=temperature()*1.8+32 # converted to deg F
    time= running_time()/1000
    print(time,temp,sep="  ")

    if temp <= 85:
        pin0.write_digital(1)
        if temp >= 84: start = 1

    elif temp >= 87:
        pin0.write_digital(0)

    else:
        pass

    sleep(1000)
    counter = counter + start

    if counter >= 120:
        pin0.write_digital(0)
        break