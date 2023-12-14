# find GCD of two numbers

a = int(input())
b = int(input())

def hcf_I(x,y):
    c = min(x,y)
    while c > 0:
        if x%c == 0 and y%c == 0:
            break
        c-=1
    return c

def hcf_II(x,y):
    while x!=y:
        if x > y:
            x=x-y
        else:
            y=y-x
    return x

def hcf_III(x,y):
    if y==0:
        return x
    else:
        return hcf_III(y,x%y)
print(hcf_I(a,b))
print(hcf_II(a,b))
print(hcf_III(a,b))