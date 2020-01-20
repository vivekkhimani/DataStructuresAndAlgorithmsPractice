'''
Description:
quickSort (Algorithm Description) - 

Average Time Complexity: 

Tip: 
'''

def quickSort(inputList,start,stop):
	if start<stop:
		p = partition(inputList,start,stop-1)
		quickSort(inputList,start,p-1)
		quickSort(inputList,p+1,stop-1)

def partition(inputList,start,stop):
	#pivot = last element
	pivot = inputList[stop-1]
	i = start
	for j in range(start,stop):
		if inputList[j] <= pivot:
			temp = inputList[i]
			inputList[i] = inputList[j]
			inputList[j] = temp
			i+=1

	temp=inputList[i]
	inputList[i]=inputList[stop-1]
	inputList[stop-1]=temp
	return i


#DRIVER
if __name__ == '__main__':
	my_list = [10,9,4,1,89,45,67,23,12,76]
	start = 0
	stop = len(my_list)
	quickSort(my_list,start,stop)
	print(my_list)
