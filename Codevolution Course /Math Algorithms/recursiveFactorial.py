def recursiveFactorial(n):
    if n == 0:
        return 1
    
    return n * recursiveFactorial(n - 1)

print(recursiveFactorial(5))
print(recursiveFactorial(4))
print(recursiveFactorial(6))