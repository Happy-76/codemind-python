l=input()
p=l.split(" ")
d=[]
for i in p:
    count=0
    for j in i:
        if j in "aeiouAEIOU":
            count=count+1
    d.append(count)
count=[]
for i in d:
    if i == max(d):
         count.append(i)
print(len(count))    