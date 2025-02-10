num1 = input()
num1 = float(num1)

num2 = input()
num2 = float(num2)

num3 = input()
num3 = float(num3)

num4 = input()
num4 = float(num4)

num5 = input()
num5 = float(num5)

num6 = input()
num6 = float(num6)

values = [num1, num2, num3, num4, num5, num6]

positive = 0

for _ in values:
    if _ > 0:
        positive += 1

print('%i valores positivos' %(positive))