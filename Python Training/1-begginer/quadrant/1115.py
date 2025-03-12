def main():
    proceed = True
    while proceed == True:
        x, y = map(int, input().split(' '))
        
        if x == 0 or y == 0:
            proceed = False
        elif x > 0 and y > 0:
            print('primeiro')
        elif x < 0 and y > 0:
            print('segundo')
        elif x < 0 and y < 0:
            print('terceiro')
        elif x > 0 and y < 0:
            print('quarto')
    
main()