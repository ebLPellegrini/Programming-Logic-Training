import math

numbers = input().split(" ")

a, b = numbers
a = int(a)
b = int(b)

if math.fmod(a, b) == 0 or math.fmod(b, a) == 0:
    print('They are multiples')
else:
    print('They are not multiples')