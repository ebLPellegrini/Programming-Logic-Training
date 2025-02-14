def main():
    total_Titans, walls_Size = map(int, input().split(" "))
    
    titans_Order = input()
    
    size_P, size_M, size_G = map(int, input().split(" "))
    
    walls = [walls_Size]
    size_dict = {'P': size_P, 'M': size_M, 'G': size_G}
    titans = [size_dict[i] for i in titans_Order]
    
    walls_Count = 1
    
    for i in range(total_Titans):
        for f in range(len(walls)): 
            if walls[f] >= titans[i]:
                walls[f] -= titans[i] 
            
                if i < total_Titans - 1:
                    if titans[i+1] > max(walls):
                        walls.append(walls_Size)
                        walls_Count += 1
                
            if walls[f] < size_P:
                walls.pop(f)

    print(walls_Count)

main()