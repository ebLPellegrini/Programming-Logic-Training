def main():
    uppercase_Input = input()
    colums = []
    rows = []
    
    for i in range(12):
        for j in range(12):
            colums.append(float(input()))
        
        rows.append(colums.copy())
        colums.clear()
        
    result = operation(uppercase_Input, rows)
    print('%.1f' %(result))

def operation(letter, storage):
    sum = 0
    
    for i in range(5,7):
        sum += storage[i][7]
        
    for i in range(4,8):
        sum += storage[i][8]
        
    for i in range(3,9):
        sum += storage[i][9]
        
    for i in range(2,10):
        sum += storage[i][10]
        
    for i in range(1,11):
        sum += storage[i][11]
        
    if letter == 'S':
        return sum
    elif letter == 'M':
        return sum/30
    else:
        return 0
    
main()