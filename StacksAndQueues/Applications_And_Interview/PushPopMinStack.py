'''
Problem Statement:
Implement a stack such that push, pop, and min operations are all executed in O(1) time

Approach:
	a) Push and Pop operations are quite straight forward and can be done in O(1) time.
	b) However, it's a bit tricky to keep a track of minimum element especially when an element is removed!

Solution:
	a) Add an attribute called minElement to the Stack object.
	b)Each time a newElement is PUSHED:
		->	If the stack is EMPTY, minElement = newElement and the newElement is pushed.
		->	If the stack is NON-EMPTY && newElement >= minElement, just push the newElement
		->	If the stack is NON-EMPTY && newElement < minElement, push newElement*2 - minElement(existing) and minElement = newElement.

	c)Each time an existingElement is POPPED:
		->	If the topElement > minElement, just pop the topElement.
		->	If the topElement <= minElement, minElement = 2*minElement - existingElement and the existingElement is popped. This helps us to get the second-most minimum element.

Why does the logic work:
	a) We store the ACTUAL minimum value in minElement when a minElement is pushed.
	b) But we store a value which is lower than the actual minimum value on the stack.
	c) We use the above mentioned formula because whenever the minimum value from the stack is removed, we can backtrace using the formula and get the previously stored minimum value.
	d) The approach is not intuitive but makes sense when you do math on paper!

Loophole:
	a) Actual minimum value would never be stored on the stack.

Status:
	Complete
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

	def getData(self):
		return int(self.__data)

	

class myStack:
	def __init__(self, head = None,minElement = None, maxSize = 20):
		self.__head = head
		self.__maxSize = maxSize
		self.__minElement = minElement

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
		return self.__head

	def push(self, newData):
		if self.isEmpty():
			self.__head = Item(newData)
			self.__minElement = int(newData)
			return

		if self.isFull():
			print("Overflow Exception")
			return
		
		#Checking for min
		if newData < self.__minElement:
			insertData = (newData)*2 - self.__minElement
			self.__minElement = newData
		
		if int(newData) >= int(self.__minElement):
			insertData = newData

		newNode = Item(insertData)
		newNode.setNext(self.__head)
		self.__head = newNode


	def pop(self):

		if self.isEmpty():
			print("Underflow Exception")
			return

		if self.returnTop() == str(self.__head.getData()):
			self.__head = None
			return self.__head

		#Checking for min
		if int(self.__head.getData()) > self.__minElement:
			pass
		if int(self.__head.getData()) <= self.__minElement:
			self.__minElement = (2*self.__minElement) - int(self.__head.getData())


		retVal = self.__head
		self.__head = self.__head.getNext()
		return retVal

	def __str__(self):
		if self.__head == None:
			return "Empty"
		ret_string = ""
		current = self.__head
		while current.getNext() != None:
			ret_string+=str(current)+"->"
			current = current.getNext()
		
		ret_string+=str(current)
		return ret_string

	def returnMin(self):
		return self.__minElement


if __name__ == "__main__":
	updatedStack = myStack()
	updatedStack.push(34)
	updatedStack.push(12)
	updatedStack.push(65)
	updatedStack.push(4)
	updatedStack.pop()
	updatedStack.push(3)
	print(updatedStack)
	print(updatedStack.returnMin())