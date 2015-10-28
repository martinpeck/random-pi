import random
import time
from sense_hat import SenseHat

# the spooky messages to display
messages = ["Happy Halloween!","SPOOKY!","Trick or treat!"]

# your message picker
def pick_message(messages):
    return messages[random.randint(0,len(messages)-1)]


# stuff to set up the HAT and clear it
sense = SenseHat()
sense.clear()
sense.set_rotation(0)


# the main loop
while True:
    
    sense.show_message(pick_messages(messages))
    time.sleep(2)
        







 
