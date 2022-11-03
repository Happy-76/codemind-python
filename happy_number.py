n=int(input())
t=n
s=0
while n>9 and n!=1 and n!=7:
    while n>0:
        r=n%10
        s+=r*r
        n//=10
    n=s
    s=0
    if n==t:
        break
if n==1 or n==7:
    print("True")
else:
    print("False")