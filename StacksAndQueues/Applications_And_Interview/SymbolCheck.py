'''
Problem Description:
Checking opening and closing of symbols (,{,},) or syntax (programming languages often require proper opening and closing of brackets).

Solution:
	a) Whenever an opening symbol is detected, PUSH it on the stack.
	b) Whenever a matching closing symbol is detected, POP the opening one from the stack.
	c) If non-matching symbol is found, return INVALID.
	d) If stack is non-empty at the end, return INVALID.
	e) If stack is empty at the end, return VALID.
'''
import sys
import os
sys.path.append(os.path.abspath('../Implementation_And_Operations'))
from StackImplementation_LinkedList import Stack

myStack = Stack()

validSample = "{Vivek Khimani} is {(<work>ing)}."
invalidSample = "{Vivek Khimani)}("
invalidSample2 = "}Vivek"

#A dictionary with key as opening tags and value as closing tags so both are mapped.
symbolDict = {"(":")","{":"}","<":">"}

def checkValid(inputString):
	for characters in inputString:
		if characters in symbolDict.keys():
			myStack.push(characters)

		elif characters in symbolDict.values():
			if myStack.isEmpty():
				return "Invalid"
			
			else:
				openTag = str(myStack.returnTop())
				if symbolDict.get(openTag) == characters:
					newPop = myStack.pop()
					#print(newPop)

	if not myStack.isEmpty():
		return "Invalid"
	return "Valid"

if __name__ == "__main__":
	print(checkValid(validSample))
	print(checkValid(invalidSample))
	print(checkValid(invalidSample2))

