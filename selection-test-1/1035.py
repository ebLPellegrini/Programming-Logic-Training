import math

numbers = input().split(" ")

a, b, c, d = numbers
a = int(a)
b = int(b)
c = int(c)
d = int(d)

if b > c and d > a:
    if (c + d) > (a + b):
        if c > 0 and d > 0:
            if math.fmod(a, 2) == 0:
                print("Valores aceitos")
            else:
                print("Valores nao aceitos")
        else:
            print("Valores nao aceitos")
    else:
        print("Valores nao aceitos")
else:
    print("Valores nao aceitos")