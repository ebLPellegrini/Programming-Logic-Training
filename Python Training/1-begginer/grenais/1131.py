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
            print('New grenal (1 - YES 2 - NO)')
            answer = int(input())
            
            if answer == 2:
                proceed = False
                valid = True
            elif answer == 1:
                valid = True
    
    print('%i grenais\nInter:%i\nGremio:%i\nDraws:%i' %(grenais, inter_Victories, gremio_Victories, draw))
    
    if inter_Victories > gremio_Victories:
        print('Inter won more games')
    elif gremio_Victories > inter_Victories:
        print('Gremio won more games')
    elif inter_Victories == gremio_Victories:
        print('There is no team that won more games')
        
main()