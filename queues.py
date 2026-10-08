#queues are data structures following the first in first out (FIFO) principle
#can be implemented using arrays or linked lists
#operations of a queue: enqueue(), dequeue(), peek(), is_empty(), size()
#example of a queue using OOP:

class Queue:
    def __init__ (self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item) #adds item to end of queue

    def isEmpty(self):
        return len(self.queue) == 0 #checks if queue is empty and returns 0 if queue is empty
    
    def dequeue(self):
        if self.isEmpty():
            return 0
        return self.queue.pop(0) #removes and returns the first item in the queue

    def peek(self):
        if self.isEmpty():
            return 0
        return self.queue[0] #square brackets to access first item in a queue without removing it

    def size(self):
        return len(self.queue) #returns the number of items in the queue

myQueue = Queue() #creating my own queue object
myQueue.enqueue(1) 
myQueue.enqueue(2)
myQueue.enqueue(3)
print(myQueue.peek())  # Output: 1
print(myQueue.size())  # Output: 3
print(myQueue.dequeue())  # Output: 1
print(myQueue.size())  # Output: 2