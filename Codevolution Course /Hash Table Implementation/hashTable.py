def main():
    table = HashTable(50)  
    table.set("name", "Bruce")
    table.set("age", 25)
    table.set("mane", "Carl")
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
        #self.table[index] = value
        bucket = self.table[index]
        if not bucket:
            self.table[index] = [[key, value]]
        else:
            sameKeyItem = next((item for item in bucket if item[0] == key), None)
            if sameKeyItem:
                sameKeyItem[1] = value
            else:
                bucket.append([key, value])
        
    def get(self, key):
        index = self.hash(key)
        #return self.table[index]
        bucket = self.table[index]
        if bucket:
            sameKeyItem = next((item for item in bucket if item[0] == key), None)
            if sameKeyItem:
                return sameKeyItem[1]
        return None
                
    def remove(self, key):
        index = self.hash(key)
        #self.table[index] = None
        bucket = self.table[index]
        if bucket:
            sameKeyItem = next((item for item in bucket if item[0] == key), None)
            if sameKeyItem:
                del bucket[bucket.index(sameKeyItem)]
        
    def display(self):
        for i in range(len(self.table)):
            if self.table[i]:
                print(i, self.table[i])
            

main()