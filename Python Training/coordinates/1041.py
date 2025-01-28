coordinates = input().split(" ")

x, y = coordinates
x = float(x)
y = float(y)

if x == 0 and y == 0:
    print('Origin')
elif x > 0 and y > 0:
    print('Q1')
elif x > 0 and y < 0:
    print('Q4')
elif x < 0 and y > 0:
    print('Q2')
elif x < 0 and y < 0:
    print('Q3')
elif x == 0:
    print('Y axis')
elif y == 0:
    print('X axis')
else:
    print('Invalid input')