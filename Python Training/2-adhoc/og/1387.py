def main():
    verification = False
    
    while verification == False:
        left, right = map(int, input().split())

        if left == 0 and right == 0:
            verification = True
            break
        
        sum = left + right
        print(sum)
    
main()