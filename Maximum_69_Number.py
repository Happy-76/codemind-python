n=input()
li=list(n)
for i in range(len(li)):
    if li[i]=='6':
        li[i]='9'
        break
print(''.join(li))