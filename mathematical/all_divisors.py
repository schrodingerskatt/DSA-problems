'''
1. Divisors always occur in pairs 
   30 : (1,30), (2,15), (3,10), (5,6)
2. One of the divisors in every pair is smaller than or equal to sqrt(n)
   For a pair (x,y)
   x*y=n
   let 'x' be the smaller. i.e. x<=y
   x*x<=n
   x<= sqrt(n)
'''
def all_divisors(n):
    sq = int(n**0.5)+1
    for i in range(1,sq,1):
        if n%i==0:
            print(i)
            if (i!=n//i): # In case of 25, if we don't add this condition, It will print [1,25,5,5] 
                # but we want [1,25,5]
                print(n//i)
a = int(input())
all_divisors(a)
'''
Another way of solving this problem is 

1. Print all divisors from 1 (inclusive) to sqrt(n) (exclusive)
2. Print all divisors from sqrt(n) (inclusive) to n (inclusive)
'''
def all_divisors_II(n):
    sq = int(n**0.5)+1
    i = 1
    while i < sq:
        if n%i==0:
            print(i)
        i+=1
    while i>=1:
        if n%i==0:
            print(n//i)
        i-=1

a = int(input())
all_divisors(a)
all_divisors_II(a) 