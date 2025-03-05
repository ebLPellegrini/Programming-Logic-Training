def main():
    luggage_Amount, conveyor_Length = map(int, input().split(' '))
    
    positions = list(map(float, input().split(' ')))
    
    speed = 11
    
    for i in range(luggage_Amount):
        if i != luggage_Amount - 1:
            calculus = positions[i+1] - positions[i]
            
            if calculus < speed:
                speed = calculus
        elif i == luggage_Amount - 1:
            parcel1 = conveyor_Length - positions[i]
            calculus = parcel1 + positions[0]
            
            if calculus < speed:
                speed = calculus

    print('%.1f' %(speed))
main()