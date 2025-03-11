def main():
    proceed = True
    
    while proceed == True:
        test_Cases = int(input())
        
        if test_Cases == 0:
            proceed = False
        else:
            division_Px, division_Py = map(int, input().split(' '))
        
            for _ in range(test_Cases):
                house_Px, house_Py = map(int, input().split(' '))
                
                if house_Px == division_Px or house_Py == division_Py:
                    print('divisa')
                elif house_Px > division_Px and house_Py > division_Py:
                    print('NE')
                elif house_Px > division_Px and house_Py < division_Py:
                    print('SE')
                elif house_Px < division_Px and house_Py < division_Py:
                    print('SO')
                elif house_Px < division_Px and house_Py > division_Py:
                    print('NO')                     
    
main()