import random

counter = 1
heads = 0

tosses = 1000

while counter <= tosses:

    coin = random.randint(0,1)
        
    if coin == 1:
        heads = heads + 1
    
    counter = counter + 1

print "There were",heads,"heads"
print "There were",tosses - heads, "tails"
print "There were",tosses,"coin tosses"


print "Percentage Heads: ", (heads / float(tosses)) * 100
print "Pecentage Tails: ", ((tosses - heads) / float(tosses)) * 100
