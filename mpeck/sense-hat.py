from sense_hat import SenseHat
import time
import random
import curses
import curses.ascii
from curses import wrapper

sense = SenseHat()

# displays a hello message on the Sense HAT's pixel display
def hello_message(name, text_colour, back_colour=[0,0,0]):
    
    sense.show_message("Hello " + name,
                       scroll_speed=0.05,
                       text_colour=text_colour,
                       back_colour=back_colour)

# causes a set of hello messages to be displayed
def greetings():
    hello_message("Jessica", [255,0,0])
    hello_message("Kathy", [0,255,0])
    hello_message("Matthew", [255,255,255]) 
    hello_message("Martin", [0,0,255])
    
# displays the letters in a word, one after another, in a random colour
def letters():

    letters = "Jessica"
    
    for letter in letters:
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)

        sense.show_letter(letter,text_colour=[r, g, b])

        time.sleep(0.5)
        
    sense.clear()
   
# scrolls the temperature
def temperature():
    temp = sense.get_temperature()
    display_message = "{:10.2f} C".format(temp)
    sense.show_message(display_message)

# displays info about the environment
def environment():

    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()

    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)

    msg = "T = %s, P=%s, H=%s" % (t,p,h)

    sense.show_message(msg, scroll_speed=0.05)

# displays some patterns on the pixel display
def pretty():


    a = [255,0,0]
    b = [0,255,0]
    c = [0,0,255]
    d = [255,255,255]
    
    for i in range(0,20):

        pattern = [
        a,a,a,a,a,a,a,a,
        a,b,b,b,b,b,b,a,
        a,b,c,c,c,c,b,a,
        a,b,c,d,d,c,b,a,
        a,b,c,d,d,c,b,a,
        a,b,c,c,c,c,b,a,
        a,b,b,b,b,b,b,a,
        a,a,a,a,a,a,a,a
        ]

        sense.set_pixels(pattern)
        time.sleep(0.1)
        a,b,c,d = b,c,d,a


    for i in range(0,20):

        pattern = [
        a,a,b,b,c,c,d,d,
        a,a,b,b,c,c,d,d,
        a,a,b,b,c,c,d,d,
        a,a,b,b,c,c,d,d,
        a,a,b,b,c,c,d,d,
        a,a,b,b,c,c,d,d,
        a,a,b,b,c,c,d,d,
        a,a,b,b,c,c,d,d
        ]

        sense.set_pixels(pattern)
        time.sleep(0.1)
        a,b,c,d = b,c,d,a

    for i in range(0,20):

        pattern = [
        a,a,a,a,a,a,a,a,
        a,a,a,a,a,a,a,a,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        c,c,c,c,c,c,c,c,
        c,c,c,c,c,c,c,c,
        d,d,d,d,d,d,d,d,
        d,d,d,d,d,d,d,d
        ]

        sense.set_pixels(pattern)
        time.sleep(0.1)
        a,b,c,d = b,c,d,a

    for i in range(0,20):

        pattern = [
        a,a,a,a,a,a,a,a,
        a,b,b,b,b,b,b,a,
        a,b,c,c,c,c,b,a,
        a,b,c,d,d,c,b,a,
        a,b,c,d,d,c,b,a,
        a,b,c,c,c,c,b,a,
        a,b,b,b,b,b,b,a,
        a,a,a,a,a,a,a,a
        ]

        sense.set_pixels(pattern)
        time.sleep(0.1)
        a,b,c,d = b,a,d,c

    sense.clear()

# scans a pixel from left to right, top to bottom
def scan_the_pixel():
    sense.clear()

    last_x = last_y = 0
    
    for y in range(0, 8) :
        for x in range (0, 8):   
            sense.set_pixel(last_x, last_y, [0,0,0])
            sense.set_pixel(x, y, [100,255,0])
            last_x = x
            last_y = y
            time.sleep(0.05)

    sense.clear()

# allows a pixel to be moved across the Sense HAT pixel display
# keys up/down/left/right move the pixel
# SPACE changes the colour of the pixel
# ESC ends things
def move_the_pixel_impl(stdscr):

    last_x = last_y = x = y = 0
    c = ""
    colour = [100,255,0]
    
    sense.clear()
    
    while c != curses.ascii.ESC:

        sense.set_pixel(x, y, colour)

        c = stdscr.getch()

        last_x, last_y = x, y
        
        if c == curses.KEY_LEFT:
            x = 7 if x == 0 else x-1 
        elif c == curses.KEY_RIGHT:
            x = 0 if x == 7 else x+1
        elif c == curses.KEY_UP:
            y = 7 if y == 0 else y-1
        elif c == curses.KEY_DOWN:
            y = 0 if y == 7 else y+1
        elif c == ord(" "):
            colour = [random.randint(50,255),
                      random.randint(50,255),
                      random.randint(50,255)]
               
        sense.set_pixel(last_x, last_y, [0,0,0])
        

    sense.clear()
    
# wrapper function that inits and closes down the curses library
def move_the_pixel():
    wrapper(move_the_pixel_impl)

     
def choose():

    choice = ""
    
    while choice != "x":   
        choice = input("Select what you want to do: ")
        if choice == "1":
            greetings()
        elif choice == "2":
            letters()
        elif choice == "3":
            temperature()
        elif choice == "4":
            environment()
        elif choice == "5":
            pretty()
        elif choice == "6":
            scan_the_pixel()
        elif choice == "7":
            move_the_pixel()


def menu():
    print("")
    print("---------------------------")
    print("-                         -")
    print("- (1) Greetings           -")
    print("- (2) Letters             -")
    print("- (3) Temperature         -")
    print("- (4) Environment         -")
    print("- (5) Pretty              -")
    print("- (6) Scan the Pixel      -")
    print("- (7) Move the Pixel      -")
    print("- (x) Exit                -")
    print("-                         -")
    print("---------------------------")
    print("")

    choose()
    
menu()


    



