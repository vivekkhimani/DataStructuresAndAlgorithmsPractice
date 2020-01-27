'''
Description: In the Josephus problem from antiquity, N people are in dire straits and agree to the following strategy to reduce the population. They arrange themselves in a circle (at positions numbered from 0 to N-1) and proceed around the circle, eliminating every Mth person until only one person is left. Legend has it that Josephus figured out where to sit to avoid being eliminated.

Use your Queue Class to solve this problem. Write a python program that takes two input N and M. Your program should print out the order in which people are eliminated (and thus would show Josephus where to sit in the circle).

Data Structure: Queue
'''
class Node:
    def __init__(self,value,next):
        self.value = value
        self.next = next
        return
    def __str__(self):
        return "[ "+str(self.value)+" ]"
    def getNext(self):
        return self.next
    def setNext(self,n):
        self.next = n
        return
    def getValue(self):
        return self.value
    def setValue(self,v):
        self.value = v
        return



#You MUST implement using your node class
class Queue:
    def __init__(self):
        self.top = None
        return
    def __str__(self):
        if self.empty():
            return "Queue Empty"

        if self.top.getNext() == None:
            return str(self.top)

        else:
            ret_str = ""
            currHead = self.top
            while currHead.getNext() != None:
                ret_str += str(currHead)
                currHead = currHead.getNext()
            return ret_str

    def front(self):
        return self.top.getValue()

    def empty(self):
        if self.top == None:
            return True
        elif self.top.getValue() == None:
            return True
        else:
            return False

    def enqueue(self,x):
        if self.empty():
            self.top = Node(x,None)
            return Node(x,None)
        currHead = self.top
        while currHead.getNext()!=None:
            currHead = currHead.getNext()

        currHead.setNext(Node(x,None))
        return Node(x,None)

    def dequeue(self):
        if self.empty():
            return None
        else:
            currHead = self.top
            newHead = self.top.getNext()
            self.top = newHead
            return currHead.value

##START##
print("The Josephus Problem")
N = int(input("Enter the Number of People in the Group:\n"))
M = int(input("Enter value for Mth Person to be killed:\n"))

q = Queue()
for items in range(0,N):
    q.enqueue(items)
counter = 1
print_arr =[]
while not q.empty():
    if (counter%M) == 0:
        print_arr.append(q.front())
        q.dequeue()
        counter+=1
    else:
        q.enqueue(q.dequeue())
        counter+=1

print("Order in which people are killed:")
for items in print_arr[0:len(print_arr)-1]:
    print(items,end=" ")

print(print_arr[-1])

