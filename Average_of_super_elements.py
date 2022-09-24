n =int(input())
lis =list(map(int,input().split()))
p =0
v =0
d =[]
for i in lis:
    if lis.count(i)==i and i not in d:
        p+=1
        v+=i
    d.append(i)
if p==0:
    print("-1")
else:
    s =v/p
    print("%.2f"%(s))
