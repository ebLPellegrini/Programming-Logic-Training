def factorial(n):
    result = 1
    
    for i in range(2, n + 1):
        result *= i
    
    return result

print(factorial(4))
print(factorial(5))
print(factorial(0))
print(factorial(1))