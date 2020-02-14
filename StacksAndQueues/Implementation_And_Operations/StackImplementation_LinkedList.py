'''
Description:
Stacks are one of the most commonly seen ADT that can be implemented using an array, list, or linked list. We have implemented it here using a Singly Linked List. The stacks are commonly identified by their LIFO (Last-In, First-Out Property). Because the item that is pushed last on the stack is the first one to be removed.

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

	def setData(self, newData):
		self.__data = newData

	

class Stack:
	def __init__(self, head = None, maxSize = 20):
		self.__head = head
		self.__maxSize = maxSize

	def isEmpty(self):
		if self.__head == None:
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

	def returnTop(self):
		current = self.__head
		while current.getNext()!=None:
			current = current.getNext()
		return str(current)

	def push(self, newData):
		if self.isEmpty():
			self.__head = Item(newData)
			return

		if self.isFull():
			print("Overflow Exception")
			return

		newNode = Item(newData)
		newNode.setNext(self.__head)
		self.__head = newNode
		

	def pop(self):
		if self.isEmpty():
			print("Underflow Exception")
			return

		if self.returnTop() == str(self.__head):
			retVal = self.__head
			self.__head = None
			return retVal

		retVal = self.__head
		self.__head = self.__head.getNext()
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

	myStack = Stack()

	myStack.push(val1)
	myStack.push(val2)
	myStack.push(val3)
	print(myStack.returnLength())
	myStack.pop()
	myStack.setSize(3)
	myStack.push(val4)
	myStack.push(val5)

	print(myStack)
