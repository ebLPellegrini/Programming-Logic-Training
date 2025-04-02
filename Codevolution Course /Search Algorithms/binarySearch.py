from math import trunc

def binarySearch(arr, target):
    leftIndex = 0
    rightIndex = len(arr) - 1
    
    while(leftIndex <= rightIndex):
        middleIndex = trunc((leftIndex + rightIndex)/2)
        
        if target == arr[middleIndex]:
            return middleIndex
        
        if target < arr[middleIndex]:
            rightIndex = middleIndex - 1 
        elif target > arr[middleIndex]:
            leftIndex = middleIndex + 1
        
    return -1
                
print(binarySearch([-5, 2, 4, 6, 10], 10))
                
        
    
# sort o array, verificar target com o do meio, se for menor verificar com os menores, se for maior verificar com os maiores,