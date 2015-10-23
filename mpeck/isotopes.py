import random

class Isotope:

    def __init__(self, change_of_decay):
        self.decayed = False
        self.chance = change_of_decay

    def test_decay(self):
        
        if not self.decayed and random.randint(1, self.chance) == 1:
            self.decayed = True
            return True
        else:
            return False
            



def decay_simulation_1():


    loops = 0
    total_isotopes = 100
    decayed_isotopes = 0



    isotopes = [Isotope(6) for x in range(1, total_isotopes+1)]



    while decayed_isotopes < total_isotopes:

        loops += 1
        
        for i in isotopes:
            if i.test_decay():
                decayed_isotopes +=1
        
        print("loop:",loops, "decayed:", decayed_isotopes)

    print("everything has decayed")
    

def decay_simulation_2():

    loops = 0
    total_isotopes = 100
    chance_of_decay = 6

    remaining_isotopes = total_isotopes

    while remaining_isotopes > 0:

        loops += 1
        
        for i in range(0, remaining_isotopes):
            if random.randint(1, chance_of_decay) == 1:
                remaining_isotopes -= 1

        print("loop:",loops, "remaining:", remaining_isotopes)

    print("everything has decayed")


decay_simulation_2()           

