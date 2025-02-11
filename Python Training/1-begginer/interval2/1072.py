def main():
    total_Inputs = input()
    total_Inputs = int(total_Inputs)
    
    inputs = []
    
    for _ in range(total_Inputs):
        inputs.append(input())
        
    numbers_In = 0
    numbers_Out = 0
        
    for i in inputs:
        i = int(i)
        if (i >= 10) and (i <= 20):
            numbers_In += 1
        else:
            numbers_Out += 1
        
    print('%i in\n%i out' %(numbers_In, numbers_Out))
    
    
main()