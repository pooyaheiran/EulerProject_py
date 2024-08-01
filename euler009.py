# https://projecteuler.net/problem=9

for a in range(100,500):
    for b in range(100,500):
        for c in range(100,500):
            if a + b + c == 1000 and (a**2) + (b**2) == (c**2):
                Answer = a * b * c
                
               
                
print(Answer)  #31875000         
                   
                    