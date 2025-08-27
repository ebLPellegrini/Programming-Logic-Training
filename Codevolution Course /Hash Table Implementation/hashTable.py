def main():
    table = HashTable(50)  
    table.set("name", "Bruce")
    table.set("age", 25)
    table.display()
    print(table.get("name"))
    table.remove("name")
    table.display()
    
class HashTable:
    def __init__(self, size):
        self.table = [None] * size
        self.size = size

    def hash(self, key):
        total = 0
        for i in key:
            total += ord(i)
        return total % self.size
    
    def set(self, key, value):
        index = self.hash(key)
        self.table[index] = value
        
    def get(self, key):
        index = self.hash(key)
        return self.table[index]
    
    def remove(self, key):
        index = self.hash(key)
        if self.table[index]:
            self.table[index] = None
        
    def display(self):
        for i in range(len(self.table)):
            if self.table[i]:
                print(i, self.table[i])
            

main()