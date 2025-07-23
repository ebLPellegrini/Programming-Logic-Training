def main():
    queue = Queue()
    print(queue.isEmpty())
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(queue.size())
    queue.printQueue()
    print(queue.dequeue())
    
class Queue:
    def __init__(self):
        self.items = {}
        self.rear = 0
        self.front = 0
    
    def enqueue(self, element):
        self.items[self.rear] = element
        self.rear += 1
        
    def dequeue(self):
        item = self.items[self.front]
        del self.items[self.front]
        self.front += 1
        return item
    
    def isEmpty(self):
        if self.rear - self.front == 0:
            return True
        else:
            return False

    def peek(self):
        return self.items[self.front]
    
    def size(self):
        return self.rear - self.front
    
    def printQueue(self):
        print(self.items)
        
main()