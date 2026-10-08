#stacks: abstract data structures following the LIFO (Last In First Out) principle
#stacks can be implemented through linked lists and arrays in python
#example of a stack implementation using a list:

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, apple):      
        self.stack.append(apple) #element 'apple' added to top of the stack

    def pop(self):
        if self.is_empty(): #checks if the stack is empty
            print('Stack is empty and cannot remove the element')
            return None
        return self.stack.pop() #the top element of the stack is removed and returned

    def peek(self):
        if self.is_empty(): #checks if stack is empty
            print('The stack is empty and cannot return the top element')
            return None
        return self.stack[-1] #the -1 returns the top element of stack without removing it

    def is_empty(self):
        return len(self.stack) == 0 #this method returns true if stack is empty and false if not

    def size(self):
        return len(self.stack) #this method returns the number of elements inside the stack


if __name__ == '__main__':
    stack1 = Stack()
    stack1.push("apple")
    stack1.push("berries")
    stack1.push("Pears")
    print(stack1.peek()) #returns the top element of the stack without removing it


#stacks using linked lists:
# linked lists are collection of nodes containing data and a reference to the next node in the sequence. 
   


        