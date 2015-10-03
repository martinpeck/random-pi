import random
import string
from datetime import datetime

# welcome the player and explain stuff

print ("Hello! I'm going to ask you some maths questions.")
print ("Let's see how many you can get right!")

# set the score to zero
score = 0



questions = int(input("how many questions: "))
table = int(input("which times table do ya want? "))

# start the timer!
start_time = datetime.now()

for question in range(1,questions + 1):
    print (" ")
    print("Question", question, ":")
    
    num1 = table
    num2 = random.randint(2,12)
    ans = num1 * num2
    
    print("What is", num1, "x", num2)
    
    answer = input("Answer: ")
    answer = answer.strip(string.whitespace)
    if answer.isdigit() == False:
        print("go to school stupid!")
    elif int(answer) == ans:
        print("Correct!")
        score = score + 1
    else:
        print("Wrong!")
        print("ha dumby the answer was",ans)




# end the timer!
end_time = datetime.now()
duration = end_time - start_time

percent = (score / questions) * 100




# print the final scores
print("")
print("----------------------------------------------------------")
print("That's all the questions done. So...what was your score...?")
print("You scored", score, "points out of a possible",questions,".")
print("You took", duration.seconds, "seconds to answer these questions.")
if percent < 50:
    print("You need to practice like a real man that does mathetematicas! dweeb!")
elif percent < 80:
    print("That's pretty good, but you could do better SILLY!")
elif percent < 100:
    print("Wow! What a maths star you are!! I'm impressed!")
elif percent == 100:
    print ("doo doo do do do do daaaaaaaa!")
