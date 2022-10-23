s=int(input())
e=0
o=0
while s>0:
    r=s%10
    if r%2==0:
        e+=1
    else:
        o+=1
    s=s//10
if e>0 and o>0:
    print('Mixed')
elif o>e:
    print('Odd')
else:
    print('Even')