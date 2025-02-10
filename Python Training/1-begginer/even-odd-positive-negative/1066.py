from math import fmod

def main():
    num1 = input()
    num1 = float(num1)
    
    num2 = input()
    num2 = float(num2)
    
    num3 = input()
    num3 = float(num3)
    
    num4 = input()
    num4 = float(num4)
    
    num5 = input()
    num5 = float(num5)
    
    numbers = [num1, num2, num3, num4, num5]
    
    even = 0
    odd = 0
    positive = 0
    negative = 0
    
    for number in numbers:
        remainder = fmod(number, 2)
        
        if remainder == 0:
            even += 1
        else:
            odd += 1
        
        if number > 0:
            positive += 1
        elif number < 0:
            negative += 1
            
    print('%i valor(es) par(es)' %(even))
    print('%i valor(es) impar(es)'%(odd))
    print('%i valor(es) positivo(s)' %(positive))
    print('%i valor(es) negativo(s)' %(negative))
    
main()