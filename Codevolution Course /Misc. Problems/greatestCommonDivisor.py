from math import fmod

def greatestCommonDivisor(a,b):
    if a > b:
        biggerNumber = a
        lowerNumber = b
    if a < b:
        biggerNumber = b
        lowerNumber = a
    if a == b:
        return a
    
    verification = True
    
    while verification == True:
        remainder = fmod(biggerNumber, lowerNumber)
        if remainder == 0:
            return lowerNumber
        else:
            biggerNumber = lowerNumber
            lowerNumber = remainder
    
print(greatestCommonDivisor(24, 18))
print(greatestCommonDivisor(48, 11))
print(greatestCommonDivisor(36, 36))