import math
def isp(n):
    if n==0 or n==1:
        return False
    s=int(math.sqrt(n))
    for i in range(2,s+1):
        if n%i==0:
            return False
    return True
n=int(input())
if isp(n):
    print("prime")
else:
    print("not a prime")