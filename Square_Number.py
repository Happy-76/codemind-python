n=int(input())
cnt = 0
for i in range(1,n//2+1,1):
    if i*i == n:
        cnt += 1
        break
if cnt == 1:
    print("True")
else:
    print("False")