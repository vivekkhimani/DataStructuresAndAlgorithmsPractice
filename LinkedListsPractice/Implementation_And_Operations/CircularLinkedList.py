#This document demonstrates how to construct a Circular List using Python and perform various operations on the Linked List.
class Node:
	def __init__(self,data=None,nextNode=None):
		self.__data = data
		self.__nextNode = nextNode
	
	def getNext(self):
		return self.__nextNode
	
	def getData(self):
		return self.__data

	def setNext(self,newNext):
		self.__nextNode = newNext
	
	def setData(self,newData):
		self.__data = newData
	
	def __str__(self):
		return str(self.getData())

class CircularLinkedList:
	def __init__(self,head=None):
		self.__head = head

	def insertHead(self,Data):
		self.__head = Node(Data)
		self.__head.setNext(self.__head)

	def insertBeforeHead(self,Data):
		current = self.__head
		while current.getNext() != self.__head:
			current = current.getNext()
		
		current.setNext(Node(Data))
		current = current.getNext()
		current.setNext(self.__head)
		self.__head = current
	
	def insertEnd(self,Data):
		current = self.__head
		while current.getNext() != self.__head:
			current = current.getNext()
		
		current.setNext(Node(Data))
		current = current.getNext()
		current.setNext(self.__head)

	def deleteEnd(self):
		current = self.__head
		while current.getNext().getNext() != self.__head:
			current = current.getNext()

		current.setNext(self.__head)
	
	def deleteHead(self):
		current = self.__head
		while current.getNext() != self.__head:
			current = current.getNext()
		
		current.setNext(self.__head.getNext())
		self.__head = self.__head.getNext()
		

	def countElements(self):
		if self.__head == None:
			return str(0)
		current = self.__head
		counter = 1
		while current.getNext() != self.__head:
			current = current.getNext()
			counter+=1
		return str(counter)

	def printList(self):
		current = self.__head
		printString = ""
		while current.getNext() != self.__head:
			printString+=str(current) + " -> "
			current = current.getNext()

		printString+=str(current) + " ->" + str(current.getNext())+"(HEAD)" 
		return printString

#Testing
if __name__ == "__main__":
	myList = CircularLinkedList()
	myList.insertHead(5)
	myList.insertEnd(10)
	myList.insertEnd(20)
	myList.insertEnd(50)
	myList.insertBeforeHead(39)
	myList.deleteEnd()
	myList.deleteHead()
	print(myList.countElements())
	print(myList.printList())