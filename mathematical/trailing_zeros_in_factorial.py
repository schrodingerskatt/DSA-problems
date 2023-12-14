''' To solve this problem we need to look out for combinations of 2 and 5, because 10 can be formed
by combination of 2 and 5. (2*5=10) since, count of 5 will be less than 2, we need to lookout only
for ocuurence of 5.
count of trailing zeros = floor(n/5)+floor(n/25)+floor(n/125)+......
'''
n = int(input())
trailing_zeros = 0
i = 5
while i <= n:
    trailing_zeros += (n // i)
    i *= 5

print(trailing_zeros)