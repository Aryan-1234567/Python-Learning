#this coding challenge asks me to create a queue class for a series of orders
#the queue then sorts the orders and checks the size of the queue and if it is empty or not

class Queue:
    def __init__ (self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def dequeue(self):
        if self.isEmpty():
            return None
        return self.queue.pop(0)

    def enqueue(self, item):
        self.queue.append(item)

    def peek(self):
        if self.isEmpty():
            return None
        return self.queue[0]

    def size(self):
        return len(self.queue)

myQueue = Queue()
myQueue.enqueue('Order101')
myQueue.enqueue('Order102')
myQueue.enqueue('Order103')
myQueue.enqueue('Order104')
print(myQueue.peek())
myQueue.enqueue("Order105")
print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.peek())
print(myQueue.size())
print(myQueue.isEmpty())