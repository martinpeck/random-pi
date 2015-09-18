#!/usr/bin/env python

import random
import RPi.GPIO as GPIO
import time

def flash_light(light, howlong):
    GPIO.output(light, True)
    time.sleep(howlong)
    GPIO.output(light, False)   

YELLOW = 11
GREEN = 13
RED = 15

# set up the GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)


print "Ho ho ho! Welcome to my naughty nice game."
name = raw_input("What's your name?: ")
print "Hello %s. Im going to tell you if youve been bad or good." % (name) 

for i in range(1, 11):
    if i % 2 == 0:
        print "thinking..."
    flash_light(RED, 0.1)    
    flash_light(GREEN, 0.1)
    #print i

    
sd = random.randrange(1,3)


if sd == 1:
    print "Youve been NAUGHTY!!!"
    flash_light(RED, 4)
elif sd == 2:
    print "Well done %s! You've been GOOD!!!" % (name)
    flash_light(GREEN, 4)

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()


    
    
