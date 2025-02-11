from math import pow

def main():
    N = int(input())

    
    if (N < 5) or (N > 2000):
        return 1
    else:
        for even in range (2, N + 1, 2):
            squared = pow(even,2)
            print('%i^2 = %.0f' %(even,squared))

main()