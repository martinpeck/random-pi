def bottles_text(num):
    if num > 1:
        return str(num) + " bottles"
    elif num == 1:
        return str(num) + " bottle"
    elif num == 0:
        return "no more bottles"
        

def ninety_nine_bottles_of_beer():
    bottle = 99
    while bottle > 0:

        
        print(bottles_text(bottle),"of beer on the wall,",bottles_text(bottle), "of beer.")
        print("Take one down and pass it around,",bottles_text(bottle - 1), "of beer on the wall.")
        bottle = bottle - 1
        
    print("No more bottles of beer on the wall, no more bottles of beer.") 
    print("Go to the store and buy some more, 99 bottles of beer on the wall.")
    



ninety_nine_bottles_of_beer()
