def main():
    arr = [-6, 20, 8, -2, 4]
    print(quickSort(arr))
    
def quickSort(arr):    
    if len(arr) < 2:
        return arr
    
    pivotElement = arr[len(arr) - 1]
    leftArr = []
    rightArr = []
    
    for i in range(len(arr) - 1):
        if arr[i] > pivotElement:
            rightArr.append(arr[i])
        else:
            leftArr.append(arr[i])
    
    return quickSort(leftArr) + [pivotElement] + quickSort(rightArr)
    
main()