from math import floor

def main():
    test_Cases = int(input())
    
    for _ in range(test_Cases):
        rows, columns = map(int, input().split())
        # the minimum number of sonars needed is the number of sonars needed to cover the row direction * the number of sonars needed to cover the colum direction
        
        sonars = floor(rows/3) * floor(columns/3)
        print(sonars)
    
main()