#1. Store numbers 2,8,4 in an array
my_NumArray = [2,4,8]

#2.  prints the elements of the array
x=0
while x < len(my_NumArray):
    print("element of my_NumArray at position ", x, "is", my_NumArray[x])
    x = x + 1

#3. store 5 as the a fourth element in the array
my_NumArray.append(5)

#4. reset the second element to 6
my_NumArray[1] = 6   


#5. uses the elements and prints the sum and the average of the elements.
x=0
sum = 0
while x < len(my_NumArray):
    sum = sum + my_NumArray[x]
    x = x + 1
print("Sum is",sum) 
print("Average is ", sum / len(my_NumArray))

