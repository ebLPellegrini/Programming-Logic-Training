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

numbers = [num1, num2, num3, num4, num5, num6]

positives = 0
positives_Sum = 0

for number in numbers:
    if number > 0:
        positives += 1
        positives_Sum += number
        
average = positives_Sum / positives

print('%i positive values' %(positives))
print('%.1f' %(average))