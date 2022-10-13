s=input()
v="aeiou"
p=[]
visit =0
for i in v:
    if i not in s and i not in p:
        p.append(v)
        visit=1
        print(i,end=" ")
if visit==0:
    print(0)