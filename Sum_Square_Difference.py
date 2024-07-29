sum1 = 0 #sum of square
square1 = 0 #square of sum

#find sum of square
for i in range(1,101):
    sum1 += i ** 2 

x = 0 
#find square of sum
for j in range(1,101):
     x += j
square1 = x**2 

#Answer
print(square1 - sum1) # 25164150