import math

def main():
    while True:
        try:
            size = int(input())
        except ValueError:
            break
        
        count = size - 1   
        arr = []
        for i in range(int(math.pow(size, 2))):
            #fulfilling the array
            arr.append(i)
            if math.fmod(i, size+1) == 0:
                arr[i] = 1
            elif math.fmod(i, size-1) == 0:
                arr[i] = 2
            else:
                arr[i] = 3
            if i == (math.pow(size, 2) - 1)/2:
                arr[i] = 2    
            if i == 0:
                arr[i] = 1
            #printing the array    
            if i == count:
                print(f'{arr[i]}')
                count += size
            else:
                print(f'{arr[i]}', end="")
                
main()