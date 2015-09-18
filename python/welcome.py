#!/usr/bin/env python

# example 2

username = raw_input("what is your name?  ")

print "welcome to the program %s" % (username)

goagain=1

while goagain == 1:

    firstnumber = int(raw_input("type the first number: "))
    secondnumber = int(raw_input("type the second number: "))

    print firstnumber, "added to", secondnumber, "equals", firstnumber + secondnumber
    print firstnumber, "minus", secondnumber, "equals", firstnumber - secondnumber
    print firstnumber, "mutiplied by", secondnumber, "equals", firstnumber * secondnumber
    
    goagain = int(raw_input("type 1 to enter more numbers,or any other number to quit: "))

print "goodbye %s come back soon" % (username)
