myList = [10,9,4,1,89,45,67,23,12,76]

#insertionSort = In place Sort
#Algorithm Description= The logic is to iterate from LEFT to RIGHT and compare every element to the element on its left. Therefore, we start with index 1 as there's no element on left of index 0. We initiate j with same value as i and keep on checking to it's left and swapping the elements until the target element reaches its correct position. 
#Time Complexity = O(n^2)
#Notes = This algorithm runs faster on the arrays which are mostly sorted as it doesn't require the SECOND loop to run and the complexity may be reduced to O(n) or O(logn)

def insertionSort(inputList):
  for i in range (1, len(inputList)):
    j = i
    while (j>0 and inputList[j-1]>inputList[j]):
      temp = inputList[j-1]
      inputList[j-1] = inputList[j]
      inputList[j]=temp
      j = j - 1

  return inputList

print(insertionSort(myList))