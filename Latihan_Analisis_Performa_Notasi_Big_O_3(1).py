import numpy as np

def getSum(myList):
    sum = 0
    for item in myList:
        sum += item
    return sum

def divideAndSum(list1, list2):
    sum_set1 = getSum(list1)
    sum_set2 = getSum(list2)
    return sum_set1, sum_set2

himpunan1 = [1, 2, 3]
himpunan2 = [6, 7, 8]
sum_list1, sum_list2 = divideAndSum(himpunan1, himpunan2)

print("Jumlah himpunan angka 1:", sum_list1)
print("Jumlah himpunan angka 2:", sum_list2)
