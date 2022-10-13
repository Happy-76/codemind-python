s =input()
p ='qwertyuioplkjhgfdsazxcvbnm'
c =0
for i in s:
    if i in p:
        c+=1
print(c)