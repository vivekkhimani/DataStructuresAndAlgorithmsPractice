'''
Description:
BinarySearch (Algorithm Description) - Look for the element at the centre, if not found, further divide the array in two parts, and keep on repeating the process until the element is found. THIS ONLY WORKS ON SORTED ARRAYS and CAN BE DONE USING RECURSION OR LOOPS

Average Time Complexity: O(logn)
'''

import math

def binarySearch(input_list,key):
    start = 0
    end = len(input_list) - 1
    while (start<=end):
        mid = (start + end)/2
        mid = math.floor(mid)

        if (input_list[mid] == key):
            return "FOUND"

        elif (key < input_list[mid]):
            end = mid-1

        elif (key > input_list[mid]):
            start = mid+1

                
    return "NOT FOUND"



##DRIVER##
my_list = [10,9,4,1,89,45,67,23,12,76]
my_list.sort()

print(binarySearch(my_list,10))
