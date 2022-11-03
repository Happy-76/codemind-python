import math
def isp(n):
    if n==0 or n==1:
        return False
    s=int(math.sqrt(n))
    for i in range(2,s+1):
        if n%i==0:
            return False
    return True
n1=int(input())
n2=int(input())
n=n1+n2
a=n+1
while True:
    if isp(a):
        break
    a+=1
print(a-n)