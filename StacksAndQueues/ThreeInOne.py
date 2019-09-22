#Implementing three stacks using a single array (similar implementation can be used for k stacks in one array. The number of elements n in an array would have to be divided with k, which will give size of individual stack)

#We will use in-built Python list objects as an array

#Initializing an array of fixed size 20 just for the sake of convenience
#We will assume it just to be an integer stack
stackArray = [0]*18

#Next we define sizes for each of the stack

#Let's assume the size of each is 6, therefore, the first stack is allocated indices 0-5, the second stack is allocated indices 6-11, third one is 12-17!



class Stack1:
	def __init__(self,pointer=0):
		self.__pointer = pointer

	def getPointer(self):
		return self.__pointer

	def incPointer(self):
		self.__pointer += 1

	def decPointer(self):
		self.__pointer -= 1

	def isEmpty(self):
		return (self.__pointer == 0)

	def isFull(self):
		return (self.__pointer == (0 + len(stackArray)/3))

	def push(self,newData):
		if self.isFull():
			print("Overflow")
			return

		stackArray[self.__pointer] = int(newData)
		self.incPointer()

	def pop(self):
		if self.isEmpty():
			print("Underflow")
			return

		retVal = stackArray[self.__pointer-1]
		stackArray[self.__pointer] = 0
		self.decPointer()
		return retVal

	def returnTop(self):
		return stackArray[self.__pointer-1]

	def __str__(self):
		i = 0
		retString = ""
		while i < self.__pointer:
			retString+=str(stackArray[i])+"->"
			i+=1
		return retString+"NULL"

#The remaining two Stacks can be implemented as different classes with same methods in same manner. The only difference will be the starting point of the pointer and the ending point. Remember, the ending point of the previous stack will be the starting point of the next one, i.e.

#Stack1 => Start = 0, End = len(arrayStack)/3 - 1
#Stack2 => Start = len(arrayStack)/3, End = (len(arrayStack)/3 * 2) - 1
#Stack3 => Start = len(arrayStack)/3 * 2, End = len(arrayStack) - 1

#The same logic can be applied for n stacks in an array!

if __name__ == "__main__":
	firstStack = Stack1()
	firstStack.push(1)
	firstStack.push(2)
	print(firstStack)
	firstStack.pop()
	print(firstStack)
	firstStack.push(3)
	firstStack.push(10)
	firstStack.push(12)
	firstStack.push(13)
	firstStack.push(15)
	print(firstStack.isEmpty())
	print(firstStack.isFull())
	firstStack.push(14)
	print(firstStack)
	print(firstStack.returnTop())


	

