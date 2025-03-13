def main():
    proceed = True
    alcohol = gasoline = diesel = 0
    
    while proceed == True:
        favorite = int(input())
        
        if favorite == 1:
            alcohol += 1
        elif favorite == 2:
            gasoline += 1
        elif favorite == 3:
            diesel += 1
        elif favorite == 4:
            proceed = False
            
    print('MUITO OBRIGADO\nAlcool: %i\nGasolina: %i\nDiesel: %i' %(alcohol, gasoline, diesel))
    
main()