first = 0
second = 1
fib_num = 0

sum = 0

while(fib_num < 4000000):
    #even number check
    if fib_num % 2 == 0: 
        sum += fib_num
    # find fibonacci number
    fib_num = second + first
    first = second
    second = fib_num
    
#Answer
print(sum) #4613732

    