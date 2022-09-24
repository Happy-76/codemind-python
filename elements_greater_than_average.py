n =int(input())
lis =list(map(int,input().split()))
p =0
a =sum(lis)//len(lis)
for i in lis:
    if i>=a:
        p+=1
print(p)
