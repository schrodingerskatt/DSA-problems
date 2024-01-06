# Problem Link : https://www.geeksforgeeks.org/encryption-validity/
import math
instruction_count = int(input())
valid_period = int(input())
n = int(input())
keys = []

for i in range(0, n):
    ele = int(input())
    keys.append(ele)  

max_divisors = 0
mp = {}

for key in keys:
    mp[key] = mp.get(key,0)+1

for i in range(len(keys)):
    key = keys[i]
    divisors = 0

    for j in range(1,int(math.sqrt(key))+1):
        if key%j == 0:
            if j in mp:
                divisors+=mp[j]
            
            if j!= key//j and key//j in mp:
                divisors+=mp[key//j]
    max_divisors = max(max_divisors, divisors)

if instruction_count*valid_period >= max_divisors*100000:
    print([1, max_divisors*100000])
else:
    print([0, max_divisors*100000])


