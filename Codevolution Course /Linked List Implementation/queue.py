import linkedListReuse

def main():
    queue = LinkedListQueue()
    queue.enqueue(0)
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.dequeue()
    print(f'Queue peek: {queue.peek()}')
    print(f'Queue is empty? {queue.isEmpty()}')
    print(f'Queue size: {queue.getSize()}')
    queue.printQueue()
    
    
class LinkedListQueue:
    def __init__(self):
        self.list = linkedListReuse.LinkedList()
    
    def enqueue(self, value):
        self.list.append(value)
        
    def dequeue(self):
        self.list.removeFromFront()
        
    def peek(self):
        return self.list.head.value
        
    def isEmpty(self):
        return self.list.isEmpty()
        
    def getSize(self):
        return self.list.getSize()
    
    def printQueue(self):
        return self.list.printList()    
    
main()