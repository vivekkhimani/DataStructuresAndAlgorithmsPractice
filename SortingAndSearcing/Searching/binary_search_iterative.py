'''
Description:
BinarySearch (Algorithm Description) - Look for the element at the centre, if not found, further divide the array in two parts, and keep on repeating the process until the element is found. THIS ONLY WORKS ON SORTED ARRAYS and CAN BE DONE USING RECURSION OR LOOPS

Time Complexity: O(logn)
'''

import math

def binarySearch(input_list,key):
    


    while len(input_list) >= 1:
        start = 0
        end = len(input_list) - 1
        mid = (start + end)/2
        mid = math.floor(mid)

        if (input_list[mid] == key):
            return "FOUND"

        elif (key < input_list[mid]):
            input_list = input_list[0:mid]

        elif (key > input_list[mid]):
            input_list = input_list[(mid+1):(end+1)]

                
    return "NOT FOUND"



##DRIVER##
my_list = [10,9,4,1,89,45,67,23,12,76]
my_list.sort()

print(binarySearch(my_list,90))
