import math
def main():
    total_inputs = int(input())
    
    for _ in range (total_inputs):
        a, b = map(int, input().split())
        if a < 10 or a > 100 or b < 10 or b > 100:
            break
        total_area = area(a,b)
        print(f'{total_area} cm2')
        
def area(a,b):
    return math.trunc(a * b / 2)

main()
