def main():
    verification = False
    
    while verification == False:
        num1, num2 = map(int, input().split())
        
        if num1 == 0 and num2 == 0:
            verification = True
            break
        
        simmetry_Difference = num2 - num1
        num3 = num1 - simmetry_Difference
        print(num3)
    
main()