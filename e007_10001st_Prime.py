# https://projecteuler.net/problem=7

# to check prime or not prime
def PrimeCheck(num):
    status = True
    for i in range(2 , num//2 + 1):
        if num % i == 0:
            status = False
    if num == 1:
        status = False
    return status

count = 0
num = 1 

while True:
    num += 1
    if PrimeCheck(num) == True:
        count += 1
        if count == 10001:
            print(num) # 104743
            break

# slow  (︶︹︺)