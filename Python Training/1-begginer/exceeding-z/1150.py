def main():
    initial = int(input())
    validation = False
    
    while validation == False:
        Z = int(input())
        
        if Z > initial:
            validation = True
    
    sum = count = 0
    while validation == True:
        sum += initial
        count += 1
        initial += 1
        
        if sum > Z:
            validation = False
    
    print(count)
    
main()