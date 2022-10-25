n=int(input())
s=n*n
r=s
s1=0
while r>0:
    e=r%10
    s1+=e
    r=r//10
if n==s1:
    print("Neon Number")
else:
    print("Not Neon Number")