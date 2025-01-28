storage = input().split(" ")

code, quantity = storage
code = int(code)
quantity = int(quantity)
total = 0

if code == 1:
    total = 4.00 * quantity
elif code == 2:
    total = 4.50 * quantity
elif code == 3:
    total = 5.00 * quantity
elif code == 4:
    total = 2.00 * quantity
elif code == 5:
    total = 1.50 * quantity
else:
    print("There is no such code")
    
print("Total: US$ %.2f" %(total))