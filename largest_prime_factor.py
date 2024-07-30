# https://projecteuler.net/problem=3

from math import ceil

#simple function to check prime numbers
def PrimeCheck(number):
    status = True
    for i in range(2,number):
        if number % i == 0:
            status = False
    
    if number == 1:
        status = False
    
    return status


num = 600851475143 
num_list = [] #save prime factors to this list

for i in range(2,ceil(num ** (1/2))):
    #condition check
    if (num) % i == 0:
        if PrimeCheck(i) == True:
            num_list.append(i)

print(num_list[-1]) #6857
