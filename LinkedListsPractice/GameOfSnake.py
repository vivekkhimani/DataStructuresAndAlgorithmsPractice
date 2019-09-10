###THE PROGRAM IS INCOMPLETE FOR NOW###


#Description: The Classical Game Of Snake is an extremely popular problem which can be broken down and solved by OBJECT-ORIENTED PROGRAMMING PRINCIPLES. I have tried to implement it using Python and have used Linked Lists to represent the Snakes. 
#Developer: Vivek Khimani
#References: https://www.geeksforgeeks.org/design-snake-game/
########################


#This class represents the single pixel on a screen. It also contains information about the exact row and column of that pixel, whether it contains snake or not, whether it contains food or not. 
import numpy as np
class SnakeNode:
	def __init__(self,rowPosition=0,columnPosition=0,nextPosition=None,positionInfo=None):
		self.__rowPosition = rowPosition
		self.__columnPosition = columnPosition
		self.__nextPosition = nextPosition
		self.__positionInfo = positionInfo

	def setPositionInfo(self,newInfo):
		self.__positionInfo = newInfo

	def setRow(self,newRow):
		self.__rowPosition = newRow
	
	def setColumn(self,newColumn):
		self.__columnPosition = newColumn
	
	def getRow(self):
		return self.__rowPosition
	
	def getColumn(self):
		return self.__columnPosition
	
	def getNextPosition(self):
		self.__nextPosition = nextPosition
	
	def getPositionInfo(self):
		self.__positionInfo = positionInfo

	def setNextPosition(self,newPosition):
		self.__nextPosition = newPosition
	
	def setPositionInfo(self,newInfo):
		self.__positionInfo = newInfo


class SnakeLinkedList:
	def __init__(self,head=None):
		self.__head = head

	def insertHead(self,rowPosition,columnPosition,positionInfo="SNAKE"):
		self.__head = SnakeNode(rowPosition,columnPosition,positionInfo)
	
	def eatFood(self,FoodRowPosition,FoodColumnPosition):
		#Food is converted to Snake's HEAD and the remaining parts are shifted back. In short, a head is added to the Snake Linked List when the food is eaten so the snake grows.
		prevHeadRow = self.__head.getRow()
		prevHeadColumn = self.__head.getColumn()
		prevHeadNextPosition = self.__head.getNextPosition()
		self.__head = SnakeNode(FoodRowPosition,FoodColumnPosition,positionInfo="SNAKE")
		self.__head.setNextPosition(SnakeNode(prevHeadRow,prevHeadColumn,prevHeadNextPosition,positionInfo="SNAKE"))

	def moveSnake(self,nextNode):
		#nextNode = SnakeNode() -> Attributes for the object are received from the game itself.
		#A Head is added to the snake and a tail is removed which allows it to move.
		prevHead = self.__head
		self.__head = nextNode()
		self.__head.setNext(prevHead)



class Board:
	#Number Explanation On The Board -> 0 represents EMPTY SPACE, 1 represents SNAKE, and 2 represents FOOD
	def __init__(self,numRows,numCols):
		self.__numRows = numRows
		self.__numCols = numCols

	myBoard = np.zeros((10,10))
	
	

		







