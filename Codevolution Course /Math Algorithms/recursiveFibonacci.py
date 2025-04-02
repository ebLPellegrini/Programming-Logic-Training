def recursiveFibonacci(n):
    if n < 2:
        return n
    
    return recursiveFibonacci(n-1) + recursiveFibonacci(n-2)
    
print(recursiveFibonacci(8))
print(recursiveFibonacci(6))