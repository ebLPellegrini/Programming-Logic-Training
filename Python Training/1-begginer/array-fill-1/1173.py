def main():
    initial = int(input())
    array = []
    
    for _ in range(10):
        array.append(initial)
        
        initial = initial * 2
        
    for index, item in enumerate(array):
        print(f'N[{index}] = {item}')
    
main()