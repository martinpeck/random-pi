#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

def turn_light_on(light):
    GPIO.output(light, True)
    time.sleep(0.15)

def turn_light_off(light):
    GPIO.output(light, False)
    time.sleep(0.15)

def flash_light(light):
    turn_light_on(light)
    turn_light_off(light)

YELLOW = 11
GREEN = 13
RED = 15
YELLOW2 = 16

# set up the GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(YELLOW2, GPIO.OUT)

while True:
    flash_light(YELLOW)
    flash_light(GREEN)
    flash_light(RED)
    flash_light(GREEN)
    flash_light(YELLOW2)
    print "Merry CHristmas ho ho ho"
    turn_light_on(YELLOW)
    turn_light_on(GREEN)
    turn_light_on(YELLOW2)
    turn_light_on(YELLOW)
    turn_light_on(GREEN)
    turn_light_on(RED)
    turn_light_on(GREEN)
    print "Hope youve been good!"
    turn_light_on(YELLOW)
    turn_light_on(YELLOW2)


    
while False:
    flash_light(YELLOW)
    flash_light(GREEN)
    flash_light(RED)    
    flash_light(GREEN)
    flash_light(YELLOW2)
    turn_light_on(YELLOW)
    turn_light_on(GREEN)
    turn_light_on(RED)
    turn_light_on(YELLOW2)
    turn_light_off(YELLOW)
    turn_light_off(GREEN)
    turn_light_off(RED)
    turn_light_off(YELLOW2)
    turn_light_on(YELLOW)
    turn_light_on(GREEN)
    turn_light_on(RED)
    turn_light_on(YELLOW2)
    turn_light_off(YELLOW)
    turn_light_off(GREEN)
    turn_light_off(RED)
    turn_light_off(YELLOW2)
    turn_light_on(GREEN)
    turn_light_on(YELLOW)
    turn_light_on(RED)
    turn_light_on(YELLOW2)
    turn_light_off(GREEN)
    turn_light_off(YELLOW)
    turn_light_off(RED)
    turn_light_off(YELLOW2)
    
    
    

    
