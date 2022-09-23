n =int(input())
lis =list(map(int,input().split()))
for i in lis:
    if i%2!=0:
        print(i,end=" ")
for j in lis:
    if j%2==0:
        print(j,end=" ")