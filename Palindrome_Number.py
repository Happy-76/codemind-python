def isp(n):
    temp=n
    s=0
    while temp>0:
        r=temp%10
        s=s*10+r
        temp//=10
    if s==n:
        return True
    else:
        return False
t=int(input())
for i in range(t):
    num=int(input())
    if isp(num):
        print("True")
    else:
        print("False")