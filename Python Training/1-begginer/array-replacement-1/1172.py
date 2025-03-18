def main():
    array = []
    for _ in range(10):
        array.append(int(input()))
        
    for index, item in enumerate(array):
        if item <= 0:
            item = 1
        
        print(f'X[{index}] = {item}')
        
main()