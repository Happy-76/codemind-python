l=input()
p=l.split(" ")
d=[]
for i in p:
    count=0
    for j in i:
        if j in "aeiouAEIOU":
            count=count+1
    d.append(count)
print(min(d))