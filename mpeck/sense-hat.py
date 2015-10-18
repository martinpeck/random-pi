from sense_hat import SenseHat
import time
import random
import curses
import curses.ascii
from curses import wrapper

sense = SenseHat()

red = [255, 0, 0]
orange = [255, 127, 0]
yellow = [255, 255, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
indigo = [75, 0, 130]
violet = [159, 0, 255]
pink = [255, 20, 120]
white = [255, 255, 255]
empty = [0, 0, 0]

text_colours = {"red": red,
                "orange": orange,
                "yellow": yellow,
                "green": green,
                "blue": blue,
                "indigo": indigo,
                "violet": violet,
                "pink": pink,
                "white": white}


# displays a hello message on the Sense HAT's pixel display
def write_message(message, text_colour=white, back_colour=[0,0,0]):
    
    sense.show_message(message,
                       scroll_speed=0.04,
                       text_colour=text_colour,
                       back_colour=back_colour)

# causes a set of hello messages to be displayed
def greetings():
    write_message("Hello Jessica", text_colour=pink)
    write_message("Hello Kathy", text_colour=green)
    write_message("Hello Matthew", text_colour=blue) 
    write_message("Hello Martin", text_colour=red)
    
# displays the letters in a word, one after another, in a random colour
def letters():
    
    message = input("message: ")

    list_of_colours = list(text_colours.values())
    while message != "exit":
        
        for letter in message:
            colour_index = random.randint(0,len(list_of_colours)-1)
            sense.show_letter(letter, text_colour = list_of_colours[colour_index])
            time.sleep(0.25)

        sense.clear()
        message = input("message: ")
   
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
    toggle = True
    
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
        elif c == ord("r"):
            colour = red
        elif c == ord("o"):
            colour = orange
        elif c == ord("y"):
            colour = yellow
        elif c == ord("g"):
            colour = green
        elif c == ord("b"):
            colour = blue
        elif c == ord("i"):
            colour = indigo
        elif c == ord("v"):
            colour = violet
        elif c == ord("p"):
            colour = pink
        elif c == ord(" "):
            toggle = not toggle

        if toggle:
            sense.set_pixel(last_x, last_y, [0,0,0])
        

    sense.clear()
    
# wrapper function that inits and closes down the curses library
def move_the_pixel():
    wrapper(move_the_pixel_impl)

def make_a_face():

    sense.clear()
    
    e = empty
    p = pink
    r = red
    o = orange
    g = green
    b = blue
    
    pattern = [
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    p,p,p,e,e,p,p,p,
    p,g,p,p,p,p,g,p,
    p,p,p,e,e,p,p,p,
    e,e,e,o,o,e,e,e,
    e,r,e,e,e,e,r,e,
    e,e,r,r,r,r,e,e,
    ]

    sense.set_pixels(pattern)

    time.sleep(5)

    pattern = [
    e,e,r,e,e,r,e,e,
    e,e,e,r,r,e,e,e,
    p,p,p,e,e,p,p,p,
    p,b,p,p,p,p,b,p,
    p,p,p,e,e,p,p,p,
    e,e,e,o,o,e,e,e,
    e,e,e,e,e,e,e,e,
    e,r,r,r,r,r,r,e,
    ]

    sense.set_pixels(pattern)

def write_messages():
    message = ""
    message = input("message: ")
    tc = green
    while message != "exit":
        if message in text_colours:
            tc = text_colours[message]
            print("changed text colour to", message)
        elif message == "colours":
            for c in text_colours:
                print(c)
        else:
            write_message(message, text_colour = tc)
            
        message = input("message: ")
        

def menu():
    print("")
    print("---------------------------")
    print("-                         -")
    print("- (0) Clear               -")
    print("- (1) Greetings           -")
    print("- (2) Letters             -")
    print("- (3) Temperature         -")
    print("- (4) Environment         -")
    print("- (5) Pretty              -")
    print("- (6) Scan the Pixel      -")
    print("- (7) Move the Pixel      -")
    print("- (8) Smiley Bob          -")
    print("- (9) Messages            -")
    print("- (x) Exit                -")
    print("-                         -")
    print("---------------------------")
    print("")


def choose():

    choice = ""
    
    while choice != "x":

        menu()
   
        choice = input("Select what you want to do: ")

        if choice == "0":
            sense.clear()
        elif choice == "1":
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
        elif choice == "8":
            make_a_face()
        elif choice == "9":
            write_messages()        

    
choose()


    



