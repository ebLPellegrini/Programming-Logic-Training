def main():
    queue = circularQueue(5)
    print(queue.isEmpty())
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.enqueue(50)
    print(queue.isFull())
    queue.printCircularQueue()
    print(queue.dequeue())
    
class circularQueue:
    def __init__(self, capacity):
        self.items = [0] * capacity
        self.capacity = capacity
        self.currentlength = 0
        self.rear = -1
        self.front = -1
    
    def isFull(self):
        return self.currentlength == self.capacity
    
    def isEmpty(self):
        return self.currentlength == 0

    def enqueue(self, element):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.items[self.rear] = element
            self.currentlength += 1
            if self.front == -1:
                self.front = self.rear
                
    def dequeue(self):
        if self.isEmpty():
            return None
        item = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.currentlength -= 1
        if self.isEmpty() == True:
            self.front = -1
            self.rear = -1
        return item
        
    def peek(self):
        if not self.isEmpty():
            return self.items[self.front]
        return None
    
    def printCircularQueue(self):
        if self.isEmpty == True:
            print('Queue is empty')
        else:
            i = 0
            string = ''
            for i in range(self.front, self.rear, (i + 1) % self.capacity):
                string += str(self.items[i]) + ' '
            string += str(self.items[(i + 1) % self.capacity])
            print(string)
                
                
main()