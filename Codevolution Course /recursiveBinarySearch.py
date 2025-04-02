from math import trunc

def recursiveBinarySearch(arr, target):
    return search(arr, target, 0, len(arr) - 1)
        
def search(arr, target, leftIndex, rightIndex):
    if leftIndex > rightIndex:
        return -1
    
    middleIndex = trunc((leftIndex + rightIndex)/2)
    
    if target == arr[middleIndex]:
        return middleIndex
    
    if target < arr[middleIndex]:
        return search(arr, target, leftIndex, middleIndex - 1)
    elif target > arr[middleIndex]:
        return search(arr, target, middleIndex + 1, rightIndex)
    
print(recursiveBinarySearch([-5, 2, 4, 6, 10], 10))