from math import fmod

def main():
    first = int(input())
    second = int(input())
    sum = 0
    
    if second > first:
        for _ in range(first, second + 1):
            if divisible_By_13(_) == True:
                sum += _
    elif first > second:
        for _ in range(second, first + 1):
            if divisible_By_13(_) == True:
                sum += _
                
    print(sum)
    
def divisible_By_13(number):
    if fmod(number, 13) != 0:
        return True
    else:
        return False
    
main()