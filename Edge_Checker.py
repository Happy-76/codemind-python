a,b = map(int,input().split())
if(b==a+1 or a==b+1 or a==b+9 or b==a+9):
    print("Yes")
else:
    print("No")