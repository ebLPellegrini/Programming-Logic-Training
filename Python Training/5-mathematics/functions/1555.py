from math import pow
def main():
    test_cases = int(input())
    for i in range (test_cases):
        x, y = map(int, input().split())
        rafael_function = pow(3 * x, 2) + pow(y, 2)
        beto_function = (2 * pow(x, 2)) + pow(5 * y, 2)
        carlos_function = ( -100 * x) + pow(y, 3)
        
        if rafael_function > beto_function and rafael_function > carlos_function:
            print('Rafael won!')
        elif beto_function > rafael_function and beto_function > carlos_function:
            print('Beto won!')
        else:
            print('Carlos won!')


main()