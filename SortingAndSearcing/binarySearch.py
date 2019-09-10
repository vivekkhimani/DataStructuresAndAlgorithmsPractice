#BinarySearch (Algorithm Description) - Look for the element at the centre, if not found, further divide the array in two parts, and keep on repeating the process until the element is found. THIS ONLY WORKS ON SORTED ARRAYS and CAN BE DONE USING RECURSION OR LOOPS
myList = [10,9,4,1,89,45,67,23,12,76]
myList.sort()

def binarySearch(inputList,key):
  firstIndex = 0
  lastIndex = len(inputList) - 1
  middle = (firstIndex + lastIndex)//2        #floor division as indexes can only have int values
  found = "NOT FOUND"

  if len(inputList) == 0:
    return found

	if key == inputList[middle]:
		found = 'FOUND'
		return found
  
	elif key < inputList[middle]:
		binarySearch(inputList[0:middle],key)
  
	elif key > inputList[middle]:
		binarySearch(inputList[(middle+1):],key)

  

print(len(
print(binarySearch(myList,76))
