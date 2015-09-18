#!/usr/bin/env python

import random
import RPi.GPIO as GPIO
import time

def insult(numberguesses):
    if numberguesses == 3:
        print "     Come on. I'm getting bored."
    elif numberguesses == 6:
        print "     Seriously. Guess it already!"
    elif numberguesses == 9:
        print "     Yawn!!!"
    elif numberguesses == 12:
        print "     I'll give you a clue. It's none of the stupid numbers you've guessed"
    elif numberguesses > 12:
        print "     You're rubbish at guessing!"

def turn_on_light(light):
    GPIO.output(light, True)
    time.sleep(2)
    GPIO.output(light, False)   

YELLOW = 11
GREEN = 13
RED = 15

# set up the GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)





secretnumber = random.randrange(1,100)
numberguesses = 0

print "I am thinking of a number between 1 and 100. Can you guess it?"

guessAgain = True

while guessAgain == True:
    
    guess = int(raw_input("What's your guess?: "))
    print ""
    
    numberguesses = numberguesses + 1

    if guess < secretnumber:
        print "Too LOW!"
        print "     You've guessed %d times" % (numberguesses)
        insult(numberguesses)
        turn_on_light(YELLOW)        
    elif guess > secretnumber:
        print "Too HIGH!"
        print "     You've guessed %d times" % (numberguesses)
        insult(numberguesses)
        turn_on_light(RED)        
    elif guess == secretnumber:
        print "Well done!!"
        print "     It took you %d guesses" % (numberguesses)
        guessAgain = False
        turn_on_light(GREEN)        
        
    print ""

print "Goodbye!!! have a good time!"
    
    
    
