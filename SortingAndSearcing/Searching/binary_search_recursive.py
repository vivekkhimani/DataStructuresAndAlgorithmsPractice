'''
Description:
BinarySearch (Algorithm Description) - Look for the element at the centre, if not found, further divide the array in two parts, and keep on repeating the process until the element is found. THIS ONLY WORKS ON SORTED ARRAYS and CAN BE DONE USING RECURSION OR LOOPS

Average Time Complexity: O(logn)

Status: Complete.
'''

import math

def search(input_list,key):
	binarySearch(input_list,key,0,len(input_list)-1)

def binarySearch(input_list,key,start,end):
	mid = (start+end)/2
	mid = math.floor(mid)

	if (start>end):
		print("NOT FOUND")
	elif (input_list[mid]==key):
		print("FOUND")
	elif (key>input_list[mid]):
		binarySearch(input_list,key,(mid+1),end)

	elif (key<input_list[mid]):
		binarySearch(input_list,key,start,(mid-1))


##DRIVER
##DRIVER##
if __name__ == '__main__':
	my_list = [10,9,4,1,89,45,67,23,12,76]
	my_list.sort()

	search(my_list,2)


