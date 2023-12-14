def power_I(x,n):
    if n==0:
        return 1
    temp = power_I(x,n//2)
    temp = temp*temp
    if n%2 == 0:
        return temp
    else:
        return temp*x
    

