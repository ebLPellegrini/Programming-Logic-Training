def main():
    pairs = int(input())
    
    for _ in range(pairs):
        dividend, divisor = map(int, input().split(' '))
        
        if divisor == 0:
            print('impossible division')
        else:
            result = float(dividend / divisor)
            print('%.1f' %(result))
    
main()