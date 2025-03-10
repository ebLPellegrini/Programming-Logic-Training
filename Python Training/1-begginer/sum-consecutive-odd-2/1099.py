from math import fmod

def main():
    test_Cases = int(input())
    last = 0
    first = 0
    sum = 0
    
    for _ in range(test_Cases):
        num1, num2 = map(int, input().split(" "))
        
        if num1 == num2:
            print('0')
        else:
            if num1 > num2:
                last = num1
                first = num2
            elif num2 > num1:
                last = num2
                first = num1
            
            
            for _ in range(first + 1, last):
                remainder = fmod(_, 2)
                if remainder == 1:
                    sum += _
    
            print(sum)
            sum = 0
        
main()