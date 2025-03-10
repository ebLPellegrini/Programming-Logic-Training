def main():
    I = 1
    
    while I < 10:
        J1 = I + 6
        J2 = I + 5
        J3 = I + 4
        
        print('I=%i J=%i' %(I, J1))
        print('I=%i J=%i' %(I, J2))
        print('I=%i J=%i' %(I, J3))
        
        I += 2
        
main()