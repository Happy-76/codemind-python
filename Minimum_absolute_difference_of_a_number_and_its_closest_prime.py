def prime(n):
    if n==0:
        return False
    s=int(n**0.5)
    for i in range(2,s+1):
        if n%i==0:
            return False
    return True
n=int(input())
r=n
m=n
while(n):
    if prime(n):
        break
    else:
        n+=1
while(m):
    if prime(m):
        break
    else:
        m-=1
print(min(r-m,n-r))