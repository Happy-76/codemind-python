def reverse(n):
    p=n
    t=0
    while p>0:
        r =p%10
        t =t*10+r
        p =p//10
    n =n+t
    return n
def palin(n):
    t=n
    v=0
    while n>0:
        r =n%10
        v =v*10+r
        n =n//10
    if v==t:
        return 1
    else:
        return 0
n =int(input())
n =reverse(n)
while(1):
    if(palin(n)):
        print(n)
        break
    else:
        n =reverse(n)
        