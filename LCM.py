a,b =map(int,input().split())
m =max(a,b)
while True:
    if m%a==0 and m%b==0:
        print(m)
        break
    m+=1
    