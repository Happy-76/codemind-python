n=int(input())
a=list(map(int,input().split()))
b=[]
p =0
for i in a:
    if i not in b and a.count(i)==i:
        p+=1
    b.append(i)
if len(b)==0:
    print(-1)
else:
    print(p)
