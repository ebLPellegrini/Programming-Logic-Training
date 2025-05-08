def longestSubstringLength(arr):
    storage = [arr[0]]
    keep = []
    repeat = False
    
    for i in range(1, len(arr)):
        for j in range(0, len(storage)):
            if arr[i] == storage[j]:
                repeat = True
                
        if repeat == False:
            storage.append(arr[i])
        else:
            keep.append(storage.copy())
            storage.clear()
            repeat = False
    
    biggestArray = []        
    for array in keep:
        if len(array) > len(biggestArray):
            biggestArray = array
    
    return len(biggestArray)        

string = 'abcdefabcbb'
print(longestSubstringLength(string))

            

        
            
            
            
                