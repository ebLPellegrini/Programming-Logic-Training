from math import fmod

def main():
    test_Cases = int(input())
    
    for _ in range(test_Cases):
        initial, total_Numbers = map(int, input().split(' '))
        count = sum = 0
        
        while count < total_Numbers:
            if is_Odd(initial) == True:
                sum += initial
                initial += 2
                count += 1
            elif is_Odd(initial) == False:
                initial += 1
        
        print(sum)
    
def is_Odd(number):
    if fmod(number, 2) == 1 or fmod(number, 2) == -1:
        return True
    else:
        return False
                
main()