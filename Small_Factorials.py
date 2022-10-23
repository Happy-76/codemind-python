def find(n):
    ft=1
    for i in range(n,0,-1):
        ft*=i
    return ft
t=int(input())
while t>0:
    n=int(input())
    fact =find(n)
    print(fact,end='
')