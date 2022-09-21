import math
def check(n):
    if n==1:
        return False
    s=int(math.sqrt(n))
    for j in range(2,s+1):
        if n%j==0:
            return False
            break
    return True
s =int(input())
e =int(input())
c=0
for i in range(s,e+1):
    if(check(i)):
        c+=1
print(c)