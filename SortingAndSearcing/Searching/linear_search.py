'''
Description:
The simplest searching algorithm in which the element is searched by iterating in-order through a data structure and checking if the required element is present or not.

Time Complexity - O(n)

Status - Complete.
'''

def linear_search(input_list,key):
    for items in input_list:
        if items == key:
            return "FOUND"

        else:
            continue
    return "NOT FOUND"

##DRIVER
my_list = [10,9,4,1,89,45,67,23,12,76]

print(linear_search(my_list,90))
