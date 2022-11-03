n=int(input())
done=0
for i in range(1,n):
    if i*i==n:
        print("True")
        done=1
if done==0:
    print("False")
