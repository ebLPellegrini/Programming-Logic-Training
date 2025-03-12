def main():
    proceed = True
    
    while proceed == True:
        total_Questions = int(input())
        
        for _ in range(total_Questions):
            A, B, C, D, E = map(int, input().split(' '))
            a_count = b_count = c_count = d_count = e_count = total_count = 0
            
            if A <= 127:
                a_count += 1
            if B <= 127:
                b_count += 1
            if C <= 127:
                c_count += 1
            if D <= 127:
                d_count += 1
            if E <= 127:
                e_count += 1
            
            total_count = a_count + b_count + c_count + d_count + e_count
            
            if total_count == 1:
                if a_count == 1:
                    print('A')
                elif b_count == 1:
                    print('B')
                elif c_count == 1:
                    print('C')
                elif d_count == 1:
                    print('D')
                elif e_count == 1:
                    print('E')
            else:
                print('*')

        if total_Questions == 0:
            proceed = False
            
main()