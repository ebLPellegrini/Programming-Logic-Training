salary = input()
salary = float(salary)
tax = 0

if salary <= 2000.00:
    print('Isento')
elif salary > 2000.00 and salary <= 3000.00:
    tax = (salary - 2000) * 0.08
    print('R$ %.2f' %(tax))
elif salary > 3000.00 and salary <= 4500.00:
    tax = (1000 * 0.08) + ((salary - 3000) * 0.18)
    print('R$ %.2f' %(tax))
elif salary > 4500.00:
    tax = (1000 * 0.08) + (1500 * 0.18) + ((salary - 4500) * 0.28)
    print('R$ %.2f' %(tax))