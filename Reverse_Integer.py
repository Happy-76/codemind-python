def reverse(n):
    s=0
    while n>0:
        r=n%10
        s=s*10+r
        n//=10
    return s
n=int(input())
rev=reverse(abs(n))
if n<0:
    print('-%d'%rev)
else:
    print(rev)