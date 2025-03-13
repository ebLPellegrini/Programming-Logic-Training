def main():
    N = int(input())
    result = 1
    
    for _ in range(N, 1, -1):
        result *= _
        
    print(result)
    
main()