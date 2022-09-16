def find(a,b):
    p=max(a,b)
    while(1):
        if p%a==0 and p%b==0:
            break
        else:
            p+=1
    return p
n = int(input())
l =list(map(int,input().split()))
lcm = find(l[0],l[1])
for i in range(2,n):
    lcm=find(lcm,l[i])
print(lcm)