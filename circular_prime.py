import math
def isp(a):
    if a==0 or a==1:
        return False
    s=int(math.sqrt(a))
    for i in range(2,s+1):
        if a%i==0:
            return False
    return True
num=int(input())
n=0
temp=num
while temp>0:
    r=temp%10
    n=n*10+r
    temp=temp//10
if isp(num) and isp(n):
        print("circular prime")
elif isp(num):
        print("prime but not a circular prime")
else:
    print("not prime")