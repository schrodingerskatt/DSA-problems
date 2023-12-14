def prime_factor(n):
    if n<=1:
        return 
    while n%2==0:
        print(2)
        n//=2
    while n%3==0:
        print(3)
        n//=3
    up = int(n**0.5)+1
    for i in range(5, up, 6):
        while n%i==0:
            print(i)
            n//=i
        while n%(i+2)==0:
            print(i+2)
            n//=(i+2)
    if n > 3:
        print(n)

num = int(input())
prime_factor(num)