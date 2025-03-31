def main():
    elements = int(input())
    
    fibonacci = [0, 1]
    
    for i in range(2, elements):
        next = fibonacci[i - 2] + fibonacci[i - 1]
        fibonacci.append(next)
    
    print(fibonacci)
    
main()