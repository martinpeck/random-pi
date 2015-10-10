
def calc_check_digit(barcode):
    
    if len(barcode) != 7:
        print "invalid length"
        exit()

    if barcode.isdigit() == False:
        print "onl12334y numbers please"
        exit()

    sum = 0
   
    mult = [3,1,3,1,3,1,3]

    for counter in range(0,7):
        char = barcode[counter]
        digit = int(char)
        outcome = digit*mult[counter]    
        sum = sum + outcome


    if sum % 10 != 0:
        next_mult_ten = (10 - (sum % 10)) + sum
    else:
        next_mult_ten = sum

    check_digit = next_mult_ten - sum

    return check_digit

def validate_barcode(full_barcode):
    if len(full_barcode) != 8:
        print "invalid length"
        exit()

    if full_barcode.isdigit() == False:
        print "only numbers please"
        exit()

    check_digit = int(full_barcode[7])

    if check_digit == calc_check_digit(full_barcode[:7]):
        return True
    else:
        return False

    
user_input = raw_input("enter a 7 digit code: ")

check_digit = calc_check_digit(user_input)

print "check digit is: " + str(check_digit)

    
user_input = raw_input("enter a 8 digit code: ")

is_valid = validate_barcode(user_input)

if is_valid:
    print "this code is valid"
else:
    print "this code is NOT valid"

    

    
