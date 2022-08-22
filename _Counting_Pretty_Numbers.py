t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    cnt =0
    for i in range(a,b+1,+1):
        if(i%10==2 or i%10==3 or i%10==9):
            cnt+=1
    print(cnt)