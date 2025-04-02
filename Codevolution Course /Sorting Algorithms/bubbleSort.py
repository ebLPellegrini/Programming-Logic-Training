def main():
    arr = [5, 4, 3, 2, 1]
    bubbleSort(arr)
    print(arr)

def bubbleSort(arr):
    while True:
        swap = False
        
        for index in range(len(arr) - 1): 
            if arr[index] > arr[index + 1]:
                storage = arr[index]
                arr[index] = arr[index + 1]
                arr[index + 1] = storage
                swap = True
                
        if swap == False:
            return arr

main()