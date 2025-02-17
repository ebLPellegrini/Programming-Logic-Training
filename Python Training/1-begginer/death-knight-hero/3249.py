def main():
    total_Battles = int(input())
    win = 0
    count_CD = 0
    
    for _ in range(total_Battles):
        battle_Attacks = input()
        
        for index, attack in enumerate(battle_Attacks):
            if attack == 'C':
                if index != len(battle_Attacks) - 1:
                    if battle_Attacks[index + 1] == 'D':
                        count_CD += 1
            
        if count_CD == 0:
            win += 1
        
        count_CD = 0
    
    print(win)
                    
main()