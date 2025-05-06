    
def permutations(arr):
    if len(arr) == 0:
        return []
    
    if len(arr) == 1:
        return [arr]
    
    storage = []
    
    for i in range(len(arr)):
        temp = arr[i]
        
        remainingArr = arr[:i] + arr[i+1:]
        
        for _ in permutations(remainingArr):
            storage.append([temp] + _)
        
    return storage

print(permutations([1, 2, 3, 4]))