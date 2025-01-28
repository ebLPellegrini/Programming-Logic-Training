current_Salary = input()
current_Salary = float(current_Salary)

rate = 0
readjustment = 0.00

if current_Salary > 0 and current_Salary <= 400.00:
    readjustment = (current_Salary * 0.15)
    rate = 15
elif current_Salary > 400.00 and current_Salary <= 800.00:
    readjustment = (current_Salary * 0.12)
    rate = 12
elif current_Salary > 800.00 and current_Salary <= 1200.00:
    readjustment = (current_Salary * 0.10)
    rate = 10
elif current_Salary > 1200.00 and current_Salary <= 2000.00:
    readjustment = (current_Salary * 0.07)
    rate = 7
elif current_Salary > 2000.00:
    readjustment = (current_Salary * 0.04)
    rate = 4
    
readjusted_Salary = current_Salary + readjustment

print('New salary: %.2f' %(readjusted_Salary))
print('Readjustment: %.2f' %(readjustment))
print('Rate: %i %%' %(rate))