# https://projecteuler.net/problem=48

sum = 0
for i in range(1,1001):
    sum = sum + (i**i)

sum = str(sum)
sum = sum[::-1]
sum = sum[0:10]

print(sum[::-1])

