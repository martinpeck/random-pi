import random
jokes = ["Why did the chicken cross the road?",
        "What did the cannibal say to the other cannibal whilst eating the clown?",
        "What do you get if you cross a kangaroo and a sheep?",
        "What did one tomato say to the other tomato?",
        "How would you feel if you got covered in perfume?",
        "How many programmers does it take to change a light bulb"]

punch_lines = ["To get to the other side!",
             "Does this taste funny to you?",
             "A wooly jummper!",
             "You run along ill catch up!",
             "Incensed!",
             "None, thats a hardware problem!"]

random_joke = random.randint(0,len(jokes)-1)

print (jokes[random_joke])
input("")
print (punch_lines[random_joke])
