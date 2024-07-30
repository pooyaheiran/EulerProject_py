
# https://projecteuler.net/problem=5


for i in range(1,999999999):
    count = 0
    for j in range(1,21):
        if i % j == 0:
            count = count + 1
        else:
            break
    if count == 20:
        print(i) #232792560
        break

#very slow
#Please help me make it better
