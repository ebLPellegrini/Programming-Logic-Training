def main():
    verification = True
    while verification == True:
        try:
            initial_Velocity, time = map(int, input().split())
        except EOFError:
            verification = False
            break
    
        if time == 0:
            print('0')
        else:
            acceleration = initial_Velocity / time
            time = time * 2
            
            displacement = round(acceleration * (time**2) / 2)
            
            print('%.0f' %(displacement))
    
main()