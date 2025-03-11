def main():
    num0 = 0
    num1 = 1    

    while num0 != num1:
        num0, num1 = map(int, input().split(" "))
        
        if num0 > num1:
            print('Decrescente')
        elif num1 > num0:
            print('Crescente')
        
main()