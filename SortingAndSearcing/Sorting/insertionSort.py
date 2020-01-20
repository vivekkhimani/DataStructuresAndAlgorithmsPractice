'''
Description:
insertionSort (Algorithm Description) - iterates the input elements by growing the sorted array at each iteration. It compares the current element with the largest value in the sorted array. If the current element is greater, then it leaves the element in its place and moves on to the next element else it finds its correct position in the sorted array and moves it to that position. 

Average Time Complexity: O(n^2)
Best Time Complexity: O(n)

Tip: Preferred manier times over more advanced algorithms (quick sort, merge sort, heap sort etc.) as it works very well on mostly sorted list. While other algorithms have same run-time as average running time.
'''


def insertionSort(inputList):
  for i in range (1, len(inputList)):
    j = i
    while (j>0 and (inputList[j-1]>inputList[j])):
      temp = inputList[j]
      inputList[j] = inputList[j-1]
      inputList[j-1]=temp
      j-=1


##DRIVER
if __name__ == '__main__':
	my_list = [10,9,4,1,89,45,67,23,12,76]
	insertionSort(my_list)
	print(my_list)