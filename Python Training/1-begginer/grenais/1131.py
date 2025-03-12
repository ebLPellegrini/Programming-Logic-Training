def main():
    proceed = True
    grenais = inter_Victories = gremio_Victories = draw = 0
    
    while proceed == True:
        inter, gremio = map(int, input().split(' '))
        grenais +=1
        
        if inter > gremio:
            inter_Victories += 1
        elif gremio > inter:
            gremio_Victories += 1
        else:
            draw += 1
            
        valid = False
        while valid == False:
            print('Novo grenal (1-sim 2-nao)')
            answer = int(input())
            
            if answer == 2:
                proceed = False
                valid = True
            elif answer == 1:
                valid = True
    
    print('%i grenais\nInter:%i\nGremio:%i\nEmpates:%i' %(grenais, inter_Victories, gremio_Victories, draw))
    
    if inter_Victories > gremio_Victories:
        print('Inter venceu mais')
    elif gremio_Victories > inter_Victories:
        print('Gremio venceu mais')
    elif inter_Victories == gremio_Victories:
        print('Nao houve vencedor')
        
main()