'''
Description:
bubbleSort (Algorithm Description) - simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.

Average Time Complexity: O(n^2)

Tip: Not frequently used in practice anymore!
'''

def bubbleSort(input_list):
	n = len(input_list)
	swapped = True
	while swapped:
		swapped = False
		for i in range(1,n):
			if input_list[i-1] > input_list[i]:
				temp = input_list[i-1]
				input_list[i-1] = input_list[i]
				input_list[i] = temp
				swapped = True


##DRIVER
if __name__ == '__main__':
	my_list = [10,9,4,1,89,45,67,23,12,76]
	bubbleSort(my_list)
	print(my_list)