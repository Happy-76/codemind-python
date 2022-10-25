n =int(input())
prd=1
s=0
while n>0:
    r=n%10
    s+=r
    prd*=r
    n=n//10
print(prd-s)