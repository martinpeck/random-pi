from sense_hat import SenseHat
import time
import random

sense = SenseHat()

def hello_message(name, text_colour, back_colour=[0,0,0]):
    
    sense.show_message("Hello " + name,
                       scroll_speed=0.05,
                       text_colour=text_colour,
                       back_colour=back_colour)

def letters():

    letters = "Jessica"
    
    for letter in letters:
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)

        sense.show_letter(letter,text_colour=[r, g, b])

        time.sleep(0.5)
        
    sense.clear()



def greetings():
    hello_message("Jessica", [255,0,0])
    hello_message("Kathy", [0,255,0])
    hello_message("Matthew", [255,255,255]) 
    hello_message("Martin", [0,0,255])
   
def temperature():
    temp = sense.get_temperature()
    display_message = "{:10.2f} C".format(temp)
    sense.show_message(display_message)

def environment():

    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()

    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)

    msg = "T = %s, P=%s, H=%s" % (t,p,h)

    sense.show_message(msg, scroll_speed=0.05)

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

def menu():
    print("")
    print("---------------------------")
    print("-                         -")
    print("- (1) Greetings           -")
    print("- (2) Letters             -")
    print("- (3) Temperature         -")
    print("- (4) Environment         -")
    print("- (5) Pretty              -")
    print("- (x) Exit                -")
    print("-                         -")
    print("---------------------------")
    print("")

    choose()
    
menu()


    



