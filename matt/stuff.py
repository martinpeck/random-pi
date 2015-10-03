import string

def do_stuff_until_something():
    keep_going = True
    
    while keep_going:
        answer = input("Who is king? ")

        if answer.lower() == "martin":
            print("correct!")
            keep_going = False
        else:
            print("wrong! try again!!!!")



def calc_square_numbers(max):
    for i in range(1, max + 1):
        print(i*i)


# do_stuff_until_something()

calc_square_numbers(5)
