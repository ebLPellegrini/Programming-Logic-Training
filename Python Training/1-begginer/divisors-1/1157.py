from math import fmod

def main():
    N = int(input())
    
    for _ in range(1, N + 1):
        if is_Divisor(N, _) == True:
            print(_)

def is_Divisor(dividend, divisor):
    if fmod(dividend, divisor) == 0:
        return True
    else:
        return False

main()