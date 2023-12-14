'''
Sqrt(n) Approach : Iterate through all numbers from 2 to square root of n and for every number check 
if it divides n [because if a number is expressed as n = xy and any of the x or y is greater than the 
root of n, the other must be less than the root value].
If we find any number that divides, we return false.

1. We will deal with a few numbers such as 1, 2, and 3, and the numbers which are divisible by 2 and 3 
   in separate cases.
2. For the remaining numbers, we iterate from 5 to sqrt(n) and check for each iteration whether 
   (that value) or (that value + 2) divides n or not and increment the value by 6 
   [because any prime can be expressed as 6n+1 or 6n-1].
3. If we find any number that divides, we return false, else true.
'''
def prime(n):
    if n <=1:
        return False
    if n==3 or n==3:
        return True
    if n%2==0 or n%3==0:
        return False
    up = int(n**0.5)+1
    for i in range(5, up, 6):
        if(n%i==0 or n%(i+2)==0):
            return False
    return True
num = int(input())
if prime(num)==True:
    print("Prime Number")
else:
    print("Not a Prime")