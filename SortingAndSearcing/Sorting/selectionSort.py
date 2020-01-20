'''
Description:
selectionSort (Algorithm Description) - This sorting algorithm is an in-place comparison-based algorithm in which the list is divided into two parts, the sorted part at the left end and the unsorted part at the right end. The smallest element is selected from the unsorted array and swapped with the leftmost element, and that element becomes a part of the sorted array. This process continues moving unsorted array boundary by one element to the right.

Average Time Complexity: O(n^2)

Tip: This algorithm is not suitable for large data sets as its average and worst case complexities are of Ο(n2), where n is the number of items.
'''

def selectionSort(input_list):
	n = len(input_list)
	for i in range(0,n-1):
		min_element = i
		for j in range(i+1,n):
			if input_list[j] < input_list[min_element]:
				min_element = j


		#swap the min with with the actual min
		temp = input_list[i]
		input_list[i] = input_list[min_element]
		input_list[min_element] = temp

##DRIVER
if __name__ == '__main__':
	my_list = [10,9,4,1,89,45,67,23,12,76]
	selectionSort(my_list)
	print(my_list)