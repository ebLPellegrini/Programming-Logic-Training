from math import pow
numbers = input().split(" ")
sides = []

for s in numbers:
    sides.append(float(s))
    
sides.sort(reverse=True)
A, B, C = sides


squaredA = pow(A, 2)
sum_squaredBC = pow(B, 2) + pow(C, 2)

if A >= B + C:
    print('THIS TRIANGLE DOES NOT EXIST')
else:
    if squaredA == sum_squaredBC:
        print('RIGHT TRIANGLE')
    elif squaredA > sum_squaredBC:
        print('OBTUSE TRIANGLE')
    elif squaredA < sum_squaredBC:
        print('ACUTE TRIANGLE')

    if A == B and B == C:
        print('EQUILATERAL TRIANGLE')
    elif (A == B and B != C) or (A == C and C != B) or (B == C and C != A):
        print('ISOSCELES TRIANGLE')