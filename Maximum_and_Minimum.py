n =int(input())
lis =list(map(int,input().split()))
d =[]
for i in lis:
    if lis.count(i)==i and i not in d:
        d.append(i)
if len(d)==0:
    print("-1")
else:
    print(min(d),max(d))
