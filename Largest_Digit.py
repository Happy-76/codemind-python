n=int(input())
mx=0
while n>0:
    r=n%10
    mx=max(r,mx)
    n//=10
print(mx)