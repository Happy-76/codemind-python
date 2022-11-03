a,b=map(int,input().split())
while a!=b:
    if a>b:
        a-=b
    elif b>a:
        b-=a
print(a)