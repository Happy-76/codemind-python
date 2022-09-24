n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if i not in b and a.count(i)==i:
        print(i,end=" ")
        b.append(i)
if len(b)==0:
    print(-1)
