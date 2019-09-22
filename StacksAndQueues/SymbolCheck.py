#Checking opening and closing of symbols (,{,},) or syntax (programming languages often require proper opening and closing of brackets) using Stacks!

#We will use the Stack already defined in the directory

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

