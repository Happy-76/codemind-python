import math
def prime(n):
    if n<=1:
        return False
    else:
        s=int(math.sqrt(n))
        for i in range(2,s+1):
            if n%i==0:
                return False
        else:
            return True
def pali(n):
    temp=n
    rev=0
    while temp>0:
        rev=rev*10+(temp%10)
        temp//=10
    if rev==n:
        return True
    else:
        return False
            
n=int(input())
i=n+1
while prime(i)==False or pali(i)==False:
    i=i+1
print(i)