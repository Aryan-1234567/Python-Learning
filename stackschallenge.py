class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.isEmpty():
            return 0
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return 0
        return self.stack[-1]

myStack = Stack()
myStack.push("Apple")
myStack.push("Banana")
myStack.push("Orange")
myStack.push("Pear")

print(myStack.peek())
print(myStack.pop())
print(myStack.pop())
print(myStack.peek())

