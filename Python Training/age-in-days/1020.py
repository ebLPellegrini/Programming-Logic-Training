import math

days = int(input())

years = 0
months = 0

if days >= 0 and days < 30:
    print("0 ano(s)\n0 mes(es)\n%i dia(s)" %(days))
else:
    years = math.trunc(days / 365)
    days = math.fmod(days, 365)
    
    months = math.trunc(days / 30)
    days = math.fmod(days, 30)
    
    print("%i ano(s)\n%i mes(es)\n%i dia(s)" %(years, months, days))