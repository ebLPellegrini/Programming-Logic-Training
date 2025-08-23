import linkedListReuse

def main():
    stack = LinkedListStack()
    stack.push(0)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
    print(f'Stack peek: {stack.peek()}')
    print(f'Stack is empty? {stack.isEmpty()}')
    print(f'Stack size: {stack.getSize()}')
    stack.printStack()

class LinkedListStack:
    def __init__(self):
        self.list = linkedListReuse.LinkedList()
        
    def push(self, value):
        self.list.prepend(value)
        
    def pop(self):
        self.list.removeFromFront()
        
    def peek(self):
        return self.list.head.value
    
    def isEmpty(self):
        return self.list.isEmpty()
    
    def getSize(self):
        return self.list.getSize()
        
    def printStack(self):
        return self.list.printList()
        
main()