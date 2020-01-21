'''
Description:
quickSort (Algorithm Description) -  It picks an element as pivot and partitions the given array around the picked pivot.

Average Time Complexity: 	O(nlogn)
Worst Case Time Complexity: O(n^2)

Tip: One of the fastest comparison-based sorting algorithm but should try and avoid using it because of its high worst-case time complexity

Status: Completed.
'''

def quickSort(inputList,start,stop):
	if start<stop:
		p = partition(inputList,start,stop)
		quickSort(inputList,start,p-1)
		quickSort(inputList,p+1,stop)

def partition(inputList,start,stop):
	#pivot = last element
	pivot = inputList[stop]
	i = start
	for j in range(start,stop):
		if inputList[j] <= pivot:
			temp = inputList[i]
			inputList[i] = inputList[j]
			inputList[j] = temp
			i+=1

	temp=inputList[i]
	inputList[i]=inputList[stop]
	inputList[stop]=temp
	return i


#DRIVER
if __name__ == '__main__':
	my_list = [10,9,4,1,89,45,67,23,12,76]
	start = 0
	stop = len(my_list) - 1
	quickSort(my_list,start,stop)
	print(my_list)
