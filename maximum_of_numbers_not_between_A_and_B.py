n =int(input())
lis =list(map(int,input().split()))
a,b =map(int,input().split())
c =0
m =0
for i in lis:
    if i<a or i>b:
        c+=1
        if m<i:
            m=i
if c==0:
    print("-1")
else:
    print(m)