import string

test1 = "Martin punched a badger!"

s = test1.lower() 
print(s)            # martin punched a badger!

s = test1.upper() 
print(s)            # MARTIN PUNCHED A BADGER!

s = test1.title() 
print(s)            # Martin Punched A Badger!

name1 = "Bob"
name2 = "Jane"

t = string.Template("$first_person loves $second_person")

s = t.substitute(first_person = name1, second_person = name2)
print(s)            # Bob loves Jane

s = t.substitute({'first_person': name2, 'second_person': name1})
print(s)            # Jane loves Bob


t = string.Template("What is $first_number x $second_number")
message = t.substitute(first_number=2, second_number=3)
print(message)
