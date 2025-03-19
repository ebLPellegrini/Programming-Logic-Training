def main():
    uppercase_Input = input()
    
    columns = []
    rows = []
    for i in range(12):
        for j in range(12):
            columns.append(float(input()))
        
        rows.append(columns.copy())
        columns.clear()
            
    result = operation(uppercase_Input, rows)
    print('%.1f' %(result))

def operation(letter, storage):
    sum = 0
    for i in range(5,7):
        sum += storage[7][i]
        
    for i in range(4,8):
        sum += storage[8][i]
        
    for i in range(3,9):
        sum += storage[9][i]
        
    for i in range(2,10):
        sum += storage[10][i]
        
    for i in range(1,11):
        sum += storage[11][i]
        
    if letter == 'S':
        return sum
    elif letter == 'M':
        return sum/30
    else:
        return 0

main()