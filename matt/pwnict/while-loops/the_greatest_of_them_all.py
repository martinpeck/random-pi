def the_greatest_of_them_all(numbers):
    counter = 0

    while counter < len(numbers):

        if counter == 0:
             bigfar = numbers[0]
        elif numbers[counter]>bigfar:
            bigfar = numbers[counter]

        counter += 1

    return bigfar

the_greatest = the_greatest_of_them_all([6,2,90,21,67,2,79,21,5,1,8,66,43])
print(the_greatest)
