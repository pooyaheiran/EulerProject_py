# https://projecteuler.net/problem=4

# append palindormic number to this list
palindormic_list = []

for i in range(100,1000):
    for j in range(100,1000):
        palindormic = i * j
        # check palindormic
        if str(palindormic)[0::] == str(palindormic)[::-1]:
            palindormic_list.append(palindormic)
            

palindormic_list.sort()
#Answer
print(palindormic_list[-1]) # 906609
