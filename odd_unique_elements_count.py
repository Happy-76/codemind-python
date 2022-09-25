n=int(input())
a=list(map(int,input().split()))
c =0
v =[]
for i in a:
    if i%2!=0 and i not in v:
        c+=1
    v.append(i)
print(c)

