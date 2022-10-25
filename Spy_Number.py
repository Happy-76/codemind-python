n=int(input())
s=0
prd=1
while n>0:
    r=n%10
    s+=r
    prd*=r
    n=n//10
if s==prd:
    print("Spy Number")
else:
    print("Not Spy Number")