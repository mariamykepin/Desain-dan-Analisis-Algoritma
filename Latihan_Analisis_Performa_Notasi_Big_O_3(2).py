import numpy as np

def getSum(myList):
    sum = 0
    for item in myList:
        sum += item 
    return sum

def subtractAndSum(set1, set2):
    result = []
    for i in range(len(set1)):
        result.append(set1[i] - set2[i])  
    sum_result = getSum(result)
    return sum_result

himpunan1 = [1, 2, 3]
himpunan2 = [6, 7, 8]
sumList = subtractAndSum(himpunan1, himpunan2)

print("Jumlah hasil pengurangan:", sumList)
