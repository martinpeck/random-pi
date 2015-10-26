x = 1
while x <= 5:
    print(x * x)
    x = x + 1



for p in range(1,6):
    print(p * p)


import random
game_won = False
ran = random.randint(1,100)

while not game_won:
    choose = int(raw_input("GIMME URE NUMBER FOOL!!!!! "))
    if choose == ran:
        print ("well done FOOL u actually know what a number is! ")
        game_won = True
    elif choose > ran:
        print ("thats bigger than my number DUMB DUMB! ")
    elif choose < ran:
        print ("thats less han my number you UTTER COMPLETE IDIOT!! ")
        
print ("the end!")

    

    
    

