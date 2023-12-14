def sieve(n):
    if n <= 1:
        return 
    is_prime=[True]*(n+1)
    for i in range(2,int(n**0.5)+1):
        if is_prime[i]:
            for j in range(2*i,n+1,i):
                is_prime[j]=False
    
    for i in range(2,n+1):
        if is_prime[i]:
            print(i,end=" ")

if __name__=="__main__":
    n=18
    sieve(n)