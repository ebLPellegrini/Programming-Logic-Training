def main():
    inputs = int(input())
    
    for _ in range(inputs):
        numbers = list(map(float, input().split(' ')))

        weighted_Average = ((numbers[0] * 2) + (numbers[1] * 3) + (numbers[2] * 5)) / 10
        
        print('%.1f' %(weighted_Average))
         
main()