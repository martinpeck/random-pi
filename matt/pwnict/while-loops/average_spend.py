def average_spend():
    spendArray = [3.12, 9.54, 8.11, 20.34, 16.71, 19.11]
    count = 0
    totalspend = 0
    while count < len(spendArray):
        totalspend = totalspend + spendArray[count]
        count += 1
    return totalspend / len(spendArray)
    
print(average_spend())

