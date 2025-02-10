from math import fmod

def main():
    num1 = input()
    num1 = int(num1)
    
    num2 = input()
    num2 = int(num2)
    
    sum = 0
    
    if num1 > num2:
        for _ in range(num2 + 1, num1):
            if fmod(_,2) != 0:
                sum += _
    elif num2 > num1:
        for _ in range (num1 + 1, num2):
            if fmod(_,2) != 0:
                sum += _
    
    print(sum)
            
main()