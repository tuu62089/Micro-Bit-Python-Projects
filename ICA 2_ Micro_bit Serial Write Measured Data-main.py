# Imports go at the top
from microbit import *

print("time_s,temp_C")

time_s=0

# Code in a 'while True:' loop repeats forever
while True:
    temp_C=temperature()
    
    print (str(time_s)+","+str(temp_C))

    time_s=time_s+2
       
    sleep(2000)