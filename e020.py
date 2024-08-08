# https://projecteuler.net/problem=20

def Factorial(num):
    sum = 1
    while num > 0:
        sum = sum * num
        num = num - 1
    return sum


def DigitAdder(num):
    sum = 0
    while num > 0:
        sum += (num % 10)
        num = num // 10
    return sum

factorial_num = Factorial(100)

print(DigitAdder(factorial_num)) # 648