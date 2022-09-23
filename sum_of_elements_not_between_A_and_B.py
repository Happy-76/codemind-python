n =int(input())
lis =list(map(int,input().split()))
a,b =map(int,input().split())
flag=0
c =0
for i in lis:
    if i<a or i>b:
        c+=i
        flag=1
if flag==10:
    print("-1")
else:
    print(c)