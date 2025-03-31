from math import fmod
def isPrime(n):
    
    if (n < 2):
        return False
    
    for i in range(2, n):
        if fmod(n, i) == 0:
            return False
            
    return True

print(isPrime(4))
print(isPrime(5))
print(isPrime(6))
print(isPrime(7))
print(isPrime(2))