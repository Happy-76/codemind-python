n=int(input())
lis=list(map(int,input().split()))
su=sum(lis)
if su%2==0:
    print(1)
else:
    print(0)