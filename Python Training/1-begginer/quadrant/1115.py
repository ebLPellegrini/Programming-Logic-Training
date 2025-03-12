def main():
    proceed = True
    while proceed == True:
        x, y = map(int, input().split(' '))
        
        if x == 0 or y == 0:
            proceed = False
        elif x > 0 and y > 0:
            print('first')
        elif x < 0 and y > 0:
            print('second')
        elif x < 0 and y < 0:
            print('third')
        elif x > 0 and y < 0:
            print('fourth')
    
main()