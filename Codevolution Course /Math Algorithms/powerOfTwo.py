from math import fmod
def isPowerOfTwo(n):
    if n < 1:
        return False
    
    while n > 1:
        if fmod(n, 2) != 0:
            return False
        
        n = n / 2
        
    return True

print(isPowerOfTwo(1))
print(isPowerOfTwo(2))
print(isPowerOfTwo(128))
print(isPowerOfTwo(24))