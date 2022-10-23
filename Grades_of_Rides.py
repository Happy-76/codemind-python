p,s,a=map(int,input().split())
if p>50 and s>60 and a>100:
    print(10)
elif p>50 and s>60:
    print(9)
elif s>60 and a>100:
    print(8)
elif p>50 and a>100:
    print(7)
elif p>50 or s>60 or a>100:
    print(6)
else:
    print(5)