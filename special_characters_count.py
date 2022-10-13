s =input().lower()
p ='qwertyuioplkj hgfdsazxcvbnm1234567890'
c =0
for i in s:
    if i not in p:
        c+=1
print(c)