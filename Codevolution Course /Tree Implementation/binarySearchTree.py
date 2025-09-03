import queueReuse

def main():
    bst = BinarySearchTree()
    print(f'Tree is empty? {bst.isEmpty()}')
    bst.insert(10)
    bst.insert(15)
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    print(bst.search(bst.root, 5))
    print(bst.search(bst.root, 15))
    print(bst.search(bst.root, 8))
    bst.delete(3)
    bst.levelOrder()
    
class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def isEmpty(self):
        return self.root == None
    
    def insert(self, value):
        newNode = Node(value)
        if self.isEmpty():
            self.root = newNode
        else:
            self.insertNode(self.root, newNode)
            
    def insertNode(self, root, newNode):
        if newNode.value < root.value:
            if root.left == None:
                root.left = newNode
            else:
                self.insertNode(root.left, newNode)
        elif newNode.value > root.value:
            if root.right == None:
                root.right = newNode
            else:
                self.insertNode(root.right, newNode)
            
    def search(self, root, value):
        if not root:
            return False
        else:
            if value == root.value:
                return True
            elif value < root.value:
                return self.search(root.left, value)
            else:
                return self.search(root.right, value)
            
    def preOrder(self, root):
        if root:
            print(root.value)
            self.preOrder(root.left)
            self.preOrder(root.right)
            
    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            print(root.value)
            self.inOrder(root.right)
            
    def postOrder(self, root):
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.value)
    
    def levelOrder(self):
        queue = queueReuse.Queue()
        queue.enqueue(self.root)
        while not queue.isEmpty():
            curr = queue.dequeue()
            print(curr.value)
            if curr.left:
                queue.enqueue(curr.left)
            if curr.right:
                queue.enqueue(curr.right)
            
    def min(self, root):
        if not root.left:
            return root.value
        else:
            return self.min(root.left)
        
    def max(self, root):
        if not root.right:
            return root.value
        else:
            return self.max(root.right)
        
    def delete(self, value):
        self.root = self.deleteNode(self.root, value)
        
    def deleteNode(self, root, value):
        if root == None:
            return root
        if value < root.value:
            root.left = self.deleteNode(root.left, value)
        elif value > root.value:
            root.right = self.deleteNode(root.right, value)
        else:
            if not root.right and not root.left:
                return None
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            root.value = self.min(root.right)
            root.right = self.deleteNode(root.right, root.value)
        return root
            
        
main()