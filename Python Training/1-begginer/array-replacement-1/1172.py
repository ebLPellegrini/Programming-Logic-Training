def main():
    array = []
    for _ in range(10):
        array.append(int(input()))
    
    count = 0    
    for item in array:
        if item <= 0:
            item = 1
        
        print(f'X[{count}] = {item}')
        count += 1
        
main()