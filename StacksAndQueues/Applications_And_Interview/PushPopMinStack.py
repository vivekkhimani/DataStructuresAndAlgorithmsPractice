#Implement a stack such that push, pop, and min operations are all executed in O(1) time

#Push and Pop operations are quite straight forward and can be done in O(1) time if the stack is implemented using a LinkedList (when pointer to the last element is maintained) or an array.

#However, it's a bit tricky to keep a track of minimum element especially when an element is removed!

#To solve this we add an attribute to the Stack called minElement. 

#Each time a newElement is PUSHED:
		#a) If the stack is EMPTY, minElement = newElement and the newElement is pushed.
		#b) If the stack is NON-EMPTY && newElement >= minElement, just push the newElement
		#c) If the stack is NON-EMPTY && newElement < minElement, push newElement*2 - minElement(existing) and minElement = newElement.

#Each time an existingElement is POPPED:
		#a) If the topElement > minElement, just pop the topElement.
		#b) If the topElement <= minElement, minElement = 2*minElement - existingElement and the existingElement is popped. This helps us to get the second-most minimum element.

#NOTE: This logic works because we store the ACTUAL VALUE of minimum in minElement when a minimum newElement is pushed. But the element that actually goes in the stack is always LESS than the actual minimum because of (2*Element - minElement). But whenever we are popping an element whose value is less than or equal to actualMin, we replace minElement with (2*minElement - popElement) . Obviously, the element which will be lesser than the minElement would have been extracted because of the first formula. This gives us the original min back. This can be better understood by drawing an actual stack on paper and doing math.

#Let's look at the LinkedList implementation. I will copy the code from previous implementation and add a min attribute to it.

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
		if int(newData) < int(self.__minElement):
			insertData = (int(newData)*2) - int(self.__minElement)
			self.__minElement = int(newData)
		
		if int(newData) >= int(self.__minElement):
			insertData = newData

	#Inserting in O(1)

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

		#For deleting in O(1) time 
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