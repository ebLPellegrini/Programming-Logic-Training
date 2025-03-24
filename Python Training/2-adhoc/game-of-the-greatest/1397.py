def main():
    verification = False
    
    while verification == False:
        rounds = int(input())
        if rounds == 0:
            verification = True
            break
        
        father = child = 0
        
        for i in range(rounds):
            left, right = map(int, input().split())
            
            if left > right:
                father += 1
            elif right > left:
                child += 1
                
        print(f'{father} {child}')
    
main()