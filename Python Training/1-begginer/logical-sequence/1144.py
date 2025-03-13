def main():
    lines = int(input())
    base = 1
    
    for _ in range(lines):
        squared_Base = base ** 2
        cubic_Base = base ** 3
        
        print('%i %i %i' %(base, squared_Base, cubic_Base))
        print('%i %i %i' %(base, squared_Base + 1, cubic_Base + 1))
        
        base += 1
    
main()