def check(n):
    a=n
    s=0
    while(n>0):
        r=n%10
        s=s*10+r
        n=n//10
    if s==a:
        return True
    return False
s=int(input())
p=int(input())
for i in range(s,p):
    if(check(i)):
        print(i,end=" ")