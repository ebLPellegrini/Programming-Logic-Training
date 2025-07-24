import math
def main():
    while True:
        a, b, c = map(int, input().split())

        if a == 0 and b == 0 and c == 0:
            break
        
        parallelepiped_volume = a * b * c
        cube_volume = math.trunc(math.pow(parallelepiped_volume, 1/3))
        print(cube_volume)
    
main()