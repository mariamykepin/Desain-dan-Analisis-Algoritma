import numpy as np

def getsum(myList):
    sum = 0
    for item in myList :
      sum = sum + item
    return sum

getsum([1,2,3])
print(getsum([1,2,3]))

getsum([1,2,3,4])
print(getsum([1,2,3,4]))