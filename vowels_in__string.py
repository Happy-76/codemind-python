s=input()
v="aeiouAEIOU"
p=[]
for i in s:
    if i in v and i not in p:
        p.append(i)
        print(i,end=" ")