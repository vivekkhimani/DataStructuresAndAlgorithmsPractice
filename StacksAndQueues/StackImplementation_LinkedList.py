#Individual Item in a stacks
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
		return current

	def push(self, newData):
		if self.isEmpty():
			self.__head = Item(newData)
			return

		if self.isFull():
			print("Overflow Exception")
			return

		current = self.__head

		while current.getNext() != None:
			current = current.getNext()

		current.setNext(Item(newData))

	def pop(self):

		if self.isEmpty():
			print("Underflow Exception")
			return

		current = self.__head

		while (current.getNext()).getNext() != None:
			current = current.getNext()

		retVal = current.getNext()
		current.setNext(None)

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


	
