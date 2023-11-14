def recursion(n):
    if n==1: # base case, here we have to stop
        print(n)
    else:
        print(n)
        recursion(n-1)

recursion(10)