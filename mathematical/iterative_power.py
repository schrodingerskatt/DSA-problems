'''
Iterative power (Binary Exponentiation)

(3)^10 = (3)^8*(3)^2    ,       10 : 1010
(3)^19 = (3)^16*(3)^2*(3)^1 ,   19: 10011

1. Every number can be written as sum of power of 2 (set bits in binary exponentiation).
2. We can traverse through all the bits of a number (from LSB to MSB) in O(log n) time.

'''

def power(x,n):
    res = 1
    while n > 0:
        if n%2==1:
            res=res*x
        x=x*x
        n/=2
    return res
print(pow(2,3))