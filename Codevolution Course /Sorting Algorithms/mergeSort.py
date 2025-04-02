from math import floor
def main():
    arr = [-6, 20, 8, -2, 4]
    print(mergeSort(arr))
    
def mergeSort(arr):
    if len(arr) < 2:
        return arr
    
    middleIndex = floor(len(arr)/2)
    leftArr = arr[:middleIndex]
    rightArr = arr[middleIndex:]
    
    return merge(mergeSort(leftArr), mergeSort(rightArr))

def merge(leftArr, rightArr):
    sortedArr = []
    while (leftArr and rightArr):
        if leftArr[0] <= rightArr[0]:
            sortedArr.append(leftArr[0])
            leftArr.remove(leftArr[0])
        else:
            sortedArr.append(rightArr[0])
            rightArr.remove(rightArr[0])
    
    return sortedArr + leftArr + rightArr
       
main()