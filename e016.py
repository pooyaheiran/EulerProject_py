# https://projecteuler.net/problem=16

def DigitAdder(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num = num // 10
    return sum

print(DigitAdder(2**1000)) # 1366
        