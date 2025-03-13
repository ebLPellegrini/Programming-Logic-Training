def main():
    validation = False
    age_Sum = count = 0
    
    while validation == False:
        individual_Age = int(input())
        
        if individual_Age < 0:
            validation = True
        else:
            age_Sum += individual_Age
            count += 1
    
    average = float(age_Sum / count)
    print('%.2f' %(average))
    
main()