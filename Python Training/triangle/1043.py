numbers = input().split(" ")

a, b, c = numbers
a = float(a)
b = float(b)
c = float(c)

if a < b + c and b < a + c and c < a + b:
    perimeter = a + b + c
    print('Perimeter = %.1f' %(perimeter))
else:
    area = (a + b) * c / 2
    print('Area = %.1f' %(area))