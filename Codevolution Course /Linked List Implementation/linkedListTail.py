def main():
    list = LinkedList()
    list.prepend(10)
    list.prepend(0)
    list.append(20)
    list.append(30)
    list.prepend(-10)
    list.removeFromEnd()
    list.removeFromFront()
    list.printList()
    print(f'List is empty? {list.isEmpty()}')
    print(f'List size: {list.getSize()}')
    
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def isEmpty(self):
        return self.size == 0
    
    def getSize(self):
        return self.size
    
    #O(1)
    def prepend(self, value):
        node = Node(value)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        
        self.size += 1
    
    #O(1)    
    def append(self, value):
        node = Node(value)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        
        self.size += 1
    
    #O(1)        
    def removeFromFront(self):
        if self.isEmpty():
            return None
        
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value
    
    #O(n)    
    def removeFromEnd(self):
        if self.isEmpty():
            return None
        
        value = self.tail.value
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            prev = self.head
            while prev.next != self.tail:
                prev = prev.next
            
            prev.next = None
            self.tail = prev
       
        self.size -= 1
        return value
        
    def printList(self):
        if self.isEmpty():
            print('List is empty!')
        else:
            current = self.head
            tempList = ''
            while current != None:
                tempList += str(current.value) + ' '
                current = current.next
            print(tempList)
            
main()