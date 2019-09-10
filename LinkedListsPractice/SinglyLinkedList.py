#This document demonstrates how to construct a Linked List using Python and perform various operations on the Linked List.

class Node:
  def __init__(self,data=None,nextNode=None):
    self.__data = data
    self.__nextNode = nextNode

  def setData(self,newData):
    self.__data = newData

  def setNext(self,newNext):
    self.__nextNode = newNext

  def getData(self):
    return self.__data

  def getNext(self):
    return self.__nextNode

  def __str__(self):
    return str(self.__data)

class SinglyLinkedList():

  def __init__(self,head=None):
    self.__head = head

  def getHead(self):
    return self.__head

  def insertNode(self,Data):
    if self.__head == None:               
      self.__head = Node(Data)
      return

    current = self.getHead()
    while current.getNext() != None:
      current = current.getNext()
    
    current.setNext(Node(Data))
  
  def insertNodeBeginning(self,Data):
    temp = self.__head
    self.__head = Node(Data)
    self.__head.setNext(temp)

  def insertNodeMiddle(self,Data,numNode):
    counter = 1
    current = self.getHead()
    while counter != (numNode - 1):
      current = current.getNext()
      counter+=1

    temp = current.getNext()
    current.setNext(Node(Data))
    current.getNext().setNext(temp)


  def calculateLength(self):
    current = self.__head
    length = 1
    while current.getNext() != None:
      length+=1
      current=current.getNext()
    
    return length

  def searchData(self,Data):
    current = self.__head
    found = "NOT FOUND"
    nodeCount = 1
    while current.getNext()!=None and found=="NOT FOUND":
      if current.getData() == Data:
        found = "FOUND"
        break
      current = current.getNext()
      nodeCount+=1

    if current.getData() == Data:
      found = "FOUND"


    return found + " at node " + str(nodeCount)

  def deleteNode(self,Data):
    current = self.__head
    prev = None
    next = current.getNext()

    while current.getNext().getData() != Data:
      prev = current
      current = current.getNext()
    
    current.setNext(current.getNext().getNext())

  def deleteFirstNode(self):
    current = self.getHead()
    self.__head = current.getNext()

  def deletingLastNode(self):
    current = self.getHead()
    prev = None

    while current.getNext() != None:
      prev = current
      current = current.getNext()
    
    prev.setNext(None)

  #deletion of the entire list can be either done by just resetting the head data and its next pointers to none. otherwise, it can also be done iteratively by traversing through every node, setting up 'temps' and freeing the node as we move ahead.
  def deletingTheEntireList(self):
    pass

  #iterative method for reversing a SINGLY linked list.
  def reversingTheListIterative(self):
    current = self.getHead()
    prev = None
    nextNode = current.getNext()

    while current != None:
      current.setNext(prev)

      prev = current
      current = nextNode
      
      if nextNode:
        nextNode = nextNode.getNext()

    self.__head = prev

  def printList(self):
    current = self.getHead()

    entireList=""
    while current.getNext() != None:
      entireList = entireList + str(current) + "->"
      current = current.getNext()

    entireList = entireList + str(current) + "-> NULL"
    print(entireList)

#Testing
if __name__ == "__main__":
	myList = SinglyLinkedList()
	myList.insertNode(4)
	myList.insertNode(8)
	myList.insertNode(12)
	myList.insertNode(18)
	myList.insertNode(54)
	myList.insertNodeMiddle(34,4)
	myList.deleteNode(12)
	myList.insertNodeMiddle(84,3)
	myList.deleteFirstNode()
	myList.deletingLastNode()
	myList.printList()
	myList.reversingTheListIterative()
	myList.printList()
	print(myList.calculateLength())
	print(myList.searchData(18))


