t=int(input())
for i in range(t):
    n=int(input())
    r=int(n**0.5)
    if r*r==n:
        print("True",end="
")
    else:
        print("False",end="
")
