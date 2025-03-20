def main():
    verification = False
    
    while verification == False:
        square_Size = int(input())
        total_Squares = 0
        
        if square_Size == 0:
            verification = True
            break
            
        for number in range(square_Size, 0, -1):
            total_Squares += (number**2)
            
        print(total_Squares)
        
main()