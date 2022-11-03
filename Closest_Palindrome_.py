def isp(n):
    t=n
    s=0
    while t>0:
        r=t%10
        s=s*10+r
        t//=10
    if s==n:
        return True
    else:
        return False
n=int(input())
a=n+1
b=n-1
while True:
    if isp(a):
        break
    a+=1
while True:
    if isp(b):
        break
    b-=1
if abs(a-n)==abs(b-n):
    print(b,a)
elif abs(a-n) > abs(b-n):
    print(b)
else:
    print(a)