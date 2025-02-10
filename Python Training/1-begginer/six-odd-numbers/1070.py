from math import fmod

def main():
    x = input()
    x = int(x)
    
    if fmod(x,2) == 0:
        x = x + 1
        for _ in range(6):
            print(x)
            x += 2
    else:
        for _ in range(6):
            print(x)
            x += 2
            
main()