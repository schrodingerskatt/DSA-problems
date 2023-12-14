
def lcm_I(x,y):
    z = max(x,y)
    while True:
        if z%x == 0 and z%y==0:
            return z
        z+=1

'''
lcm(x,y)=(x*y)/gcd(x,y)
'''

def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y,x%y)
def lcm_II(x,y):
    return (x*y)//gcd(x,y)

a = int(input())
b = int(input())
print(lcm_I(a,b))
print(lcm_II(a,b))
    