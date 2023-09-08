def  getSum(myList):
  sum = 0
  for row in myList :
    for item in row :
      sum += item
  return sum

getSum([[1,2,5],[3,4,7]])
print(getSum([[1,2,5],[3,4,7]]))

getSum([[1,2],[3,4]])
print(getSum([[1,2],[3,4]]))

getSum([[1,2,3],[4,5,6]])
print(getSum([[1,2,3],[4,5,6]]))