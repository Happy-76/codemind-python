def check(n):
    s=n//k
    if s*k==n:
        return True
    return False
l,r,k =map(int,input().split())
c=0
for i in range(l,r+1):
    if(check(i)):
        c+=1
print(c)
