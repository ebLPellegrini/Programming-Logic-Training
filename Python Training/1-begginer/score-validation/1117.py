def main():
    proceed = True
    sum = 0
    i = 0
    
    while proceed == True:
        score = float(input())
        
        if score < 0 or score > 10:
            print('invalid score')
        else:
            i += 1
            sum += score
            
        if i == 2:
            proceed = False
            
    average = float(sum / 2)
    print('average = %.2f' %(average))
    
main()