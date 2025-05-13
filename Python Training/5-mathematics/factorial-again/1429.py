def main():
    while True:
        number = input()
        if int(number) == 0:
            return
        
        sum = 0
        number = number[::-1]
        for index, digit in enumerate(number):
            sum += int(digit) * factorial(index + 1)

        print(sum)

def factorial(num):
    if num == 0 or num == 1:
        return 1
    
    if num == 2:
        return 2
    
    return num * factorial(num - 1)

main()