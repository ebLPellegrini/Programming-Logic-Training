def main():
    list = LinkedList()
    list.prepend(10)
    list.prepend(20)
    list.prepend(30)
    list.printList()
    list.append(0)
    list.insert(5,3)
    list.printList()
    list.removeFrom(3)
    list.printList()
    list.reverse()
    list.printList()
    print(f'List is empty? {list.isEmpty()}')
    print(f'List size: {list.getSize()}')
    print(f'Index of 10: {list.search(10)}')
    
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
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
        else:
            node.next = self.head
            self.head = node
        self.size += 1
    
    #O(n)
    def append(self, value):
        node = Node(value)
        if self.isEmpty():
            self.head = node
        else:
            previous = self.head
            while previous.next != None:
                previous = previous.next
            previous.next = node
            self.size += 1
           
    def insert(self, value, index):
        if index > self.size or index < 0:
            print('Invalid index')
            return
        elif index == 0:
            self.prepend(value)
        else:
            node = Node(value)
            temp = self.head
            for i in range(index - 1):
                temp = temp.next
            node.next = temp.next
            temp.next = node
            self.size += 1
               
    def removeFrom(self, index):
        if index < 0 or index >= self.size:
            print('Invalid index')
            return None
        removedNode = self.head
        if index == 0:
            removedNode = self.head
            self.head = self.head.next
            return removedNode
        else:
            temp = self.head
            for i in range(index - 1):
                temp = temp.next
            removedNode = temp.next
            temp.next = removedNode.next
        self.size -= 1
        return removedNode.value
            
    def search(self, value):
        if self.isEmpty():
            return -1
        index = 0
        temp = self.head
        while(temp):
            if temp.value == value:
                return index
            temp = temp.next
            index += 1
        return -1
    
    def reverse(self):
        prev = None
        curr = self.head
        while(curr):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
        
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