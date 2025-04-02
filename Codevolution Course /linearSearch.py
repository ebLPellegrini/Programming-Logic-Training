def main():
    array = map(int, input().split())
    print('What is the target element?')
    target = int(input())
    
    for index, element in enumerate(array):
        if element == target:
            return index
            
    return -1
        
print(main())