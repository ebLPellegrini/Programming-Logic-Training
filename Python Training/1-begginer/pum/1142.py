def main():
    lines = int(input())
    a = 1
    b = 2
    c = 3
    
    for _ in range(lines):
        print('%i %i %i PUM' %(a, b, c))
        a += 4
        b += 4
        c += 4
        
main()