DDD = input()
DDD = int(DDD)

DDDdict = {
    "61": "Brasilia",
    "71": "Salvador",
    "11": "Sao Paulo",
    "21": "Rio de Janeiro",
    "32": "Juiz de Fora",
    "19": "Campinas",
    "27": "Vitoria",
    "31": "Belo Horizonte"
}

if DDD == 61:
    print(DDDdict["61"])
elif DDD == 71:
    print(DDDdict["71"])
elif DDD == 11:
    print(DDDdict["11"])
elif DDD == 21:
    print(DDDdict["21"])
elif DDD == 32:
    print(DDDdict["32"])
elif DDD == 19:
    print(DDDdict["19"])
elif DDD == 27:
    print(DDDdict["27"])
elif DDD == 31:
    print(DDDdict["31"])
else:
    print("DDD not found")