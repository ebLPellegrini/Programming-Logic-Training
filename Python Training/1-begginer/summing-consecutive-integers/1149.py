def main():
    request = list(map(int, input().split()))
    initial = request[0]
    N = sum = 0
    
    for _ in range(1, len(request)):
        if request[_] > 0:
            N = request[_]
    
    for _ in range(N):
        sum += initial
        initial += 1
    
    print(sum)
    
main()