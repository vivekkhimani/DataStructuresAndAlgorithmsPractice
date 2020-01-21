'''
Description: It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves.
mergeSort (Algorithm Description) - 

Average Time Complexity: 	O(nlogn)
Worse Case Time Complexity: O(nlogn)

Tip: Can be used often because of same worst-case complexity.

Status: Completed
'''

def mergeSort(A,start,stop):
	if start<stop:
		middle = start + ((stop-start)//2)
		mergeSort(A,start,middle)
		mergeSort(A,middle+1,stop)
		merge(A,start,middle,stop)

	else:
		return

def merge(A,start,middle,stop):
	aux_array = [0]*len(A)
	for k in range(start,stop+1):
		aux_array[k] = A[k]
	i = start
	j = middle + 1
	for k in range(start,stop+1):
		if i>middle:
			A[k] = aux_array[j]
			j+=1
			continue

		elif j>stop:
			A[k] = aux_array[i]
			i+=1
			continue

		elif aux_array[j]>aux_array[i]:
			A[k] = aux_array[i]
			i+=1
			continue

		else:
			A[k] = aux_array[j]
			j+=1
			continue

#DRIVER
if __name__ == '__main__':
	my_list = [10,9,4,1,89,45,67,23,12,76]
	start = 0
	stop = len(my_list) - 1
	mergeSort(my_list,start,stop)
	print(my_list)