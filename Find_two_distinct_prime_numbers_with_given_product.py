import math
def prime(k):
    if k<2:
        return False
    else:
        s=int(math.sqrt(k))
        for i in range(2,s+1):
            if k%i==0:
                return False
        return True
def find(n):
    m=0
    s=int(math.sqrt(n))
    for i in range(2,s+1):
        if n%i==0:
            m=n//i
            if prime(i) and prime(m):
                return i,m
    return [-1]
n=int(input())
print(*find(n))