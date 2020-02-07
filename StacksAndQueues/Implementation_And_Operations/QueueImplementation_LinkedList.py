'''
Description:
Queue are one of the most commonly seen ADT that can be implemented using an array, list, or linked list. We have implemented it here using a Singly Linked List. The queues are commonly identified by their FIFO (First-In, First-Out Property). Because the item that is pushed first in the queue is the first one to be served.

Data Structure Used:
	Linked List

Average Time Complexity:
	Access=O(n)
	Search=O(n)
	Insertion=O(1)
	Deletion=O(1)

Worst Time Complexity:
	Access=O(n)
	Search=O(n)
	Insertion=O(1)
	Deletion=O(1)

Status: Complete.
'''
class Item:
	def __init__(self, data = None, nextItem = None):
		self.__data = data
		self.__nextItem = nextItem
	
	def __str__(self):
		return str(self.__data)

	def getNext(self):
		return self.__nextItem
	
	def setNext(self, newItem):
		self.__nextItem = newItem


class Queue:
	def __init__(self, head = None, maxSize = 20, last = None):
		self.__head = head
		self.__maxSize = maxSize
		self.__last = last

	def isEmpty(self):
		if self.__head == None and self.__last == None:
			return True
		return False

	def setSize(self,newSize):
		self.__maxSize = newSize

	def returnLength(self):
		current = self.__head
		len_counter = 1

		while current.getNext() != None:
			len_counter+=1
			current = current.getNext()
		return len_counter

	def isFull(self):
		if self.returnLength() == self.__maxSize:
			return True
		return False

	def returnLast(self):
		return self.__last

	def returnFirst(self):
		return self.__head

	def push(self, newData):
		if self.isEmpty():
			self.__head = Item(newData)
			self.__last = Item(newData)
			return

		if self.isFull():
			print("Overflow Exception")
			return

		else:
			self.__last.setNext(Item(newData))
			self.__last = self.__last.getNext()

	def pop(self):

		if self.isEmpty():
			print("Underflow Exception")
			return


		retVal = self.__head
		self.__head = self.__head.getNext()

		if self.__head == None:
			self.__last = None

		return retVal

	def __str__(self):
		ret_string = ""
		current = self.__head
		while current.getNext() != None:
			ret_string+=str(current)+"->"
			current = current.getNext()
		
		ret_string+=str(current)

		return ret_string

if __name__ == '__main__':
	val1 = Item(25)
	val2 = Item(23)
	val3 = Item(10)
	val4 = Item(8)
	val5 = Item(7)

	myQ = Queue()

	myQ.push(val1)
	myQ.push(val2)
	myQ.push(val3)
	print(myQ.returnLength())
	myQ.pop()
	myQ.setSize(3)
	myQ.push(val4)
	myQ.push(val5)

	print(myQ)