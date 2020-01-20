#This document demonstrates how to construct a Doubly Linked List using Python and perform various operations on the Linked List.

class Node:
  def __init__(self,data=None,nextNode=None,prevNode=None):
    self.__data = data
    self.__nextNode = nextNode
    self.__prevNode = prevNode

  def getData(self):
    return self.__data

  def getPrev(self):
    return self.__prevNode

  def getNext(self):
    return self.__nextNode

  def setData(self,newData):
    self.__data = newData
  
  def setPrev(self,newPrev):
    self.__prevNode = newPrev

  def setNext(self,newNext):
    self.__nextNode = newNext

  def __str__(self):
    return str(self.getData())

class DoublyLinkedList():
  def __init__(self,head=None):
    self.__head = head

  def insertHead(self,Data):
    self.__head = Node(Data)

  def insertBeforeHead(self,Data):
    current = self.__head
    current.setPrev(Node(Data))
    current = current.getPrev()
    current.setNext(self.__head)
    self.__head = current
  
  def insertAfterTail(self,Data):
    current = self.__head
    while current.getNext()!=None:
      current = current.getNext()
    current.setNext(Node(Data))
    temp = current
    current = current.getNext()
    current.setPrev(temp)

  def SearchElement(self,Data):
    current = self.__head
    counter = 1
    while current != None:
      if current.getData() == Data:
        return "FOUND AT " + str(counter)
      current = current.getNext()
      counter+=1
    return "NOT FOUND"

  def deletingTheFirstNode(self):
    newHead = self.__head.getNext()
    self.__head = newHead
    newHead.setPrev(Node())

  def deleteFromMiddle(self,numNode):
  	current = self.__head
    counter=1
    while counter!=numNode:
      current = current.getNext()
      counter+=1

    temp = current.getNext()
    current = current.getPrev()
    current.setNext(temp)
    temp.setPrev(current)

  def deletingTheLastNode(self):
    current = self.__head
    while current.getNext() != None:
      current = current.getNext()

    current = current.getPrev()
    current.setNext(Node())

  def reversingDoublyLinkedList(self):
    current = self.__head
    prev = current.getPrev()
    nextNode = current.getNext()

    while current!=None:
      tempNext = current.getNext()
      tempPrev = current.getPrev()
      current.setNext(prev)
      current.setPrev(nextNode)

      prev = current
      current = tempNext
      
      if nextNode:
        nextNode = tempNext.getNext()
      
      self.__head = prev

  def printList(self):
    printString = "NULL <-> " 
    current = self.__head
    while current!= None:
      printString += str(current) + " <-> "
      current = current.getNext()
    
    printString+="NULL"
    return printString

#Testing
if __name__ == "__main__":
	myList = DoublyLinkedList()
	myList.insertHead(4)
	myList.insertBeforeHead(3)
	myList.insertAfterTail(5)
	myList.insertAfterTail(8)
	myList.insertAfterTail(20)
	myList.insertAfterTail(30)
	print(myList.printList())
	myList.reversingDoublyLinkedList()
	print(myList.printList())
	print(myList.SearchElement(8))