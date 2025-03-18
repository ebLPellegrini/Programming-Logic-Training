def main():
    limit = int(input())
    array = []
    
    while len(array) < 1000:
        for _ in range(limit):
            array.append(_)
            
    for index, item in enumerate(array):
        if index < 1000:
            print(f'N[{index}] = {item}')

main()