myList = [4,9,1,3,87,34,12,98,43,78,94]
##########

#QuickSort is a highly efficient algorithm which usually runs in nlogn time (faster than insertion sort which runs in n^2). But, when the number of elements in the array are small or mostly sorted, it's usually beneficial to use INSERTION sort as it's faster. 

#Quicksort is divided in two functions -> PARTITIONS and SORTING using those partitions

def partition(myList):
	pivotPointer = len(myList)-1
	first = 0

	while i < pivotPointer