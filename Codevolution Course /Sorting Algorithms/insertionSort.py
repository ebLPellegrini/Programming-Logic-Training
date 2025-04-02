def main():
    arr = [5, 4, 3, 2, 1]
    insertionSort(arr)
    print(arr)
    
def insertionSort(arr):
        for i in range(1, len(arr)):
            elementToInsert = arr[i]
            j = i - 1
            
            while j >= 0 and arr[j] > elementToInsert:
                arr[j+1] = arr[j]
                j = j - 1
                
            arr[j+1] = elementToInsert
        
main()