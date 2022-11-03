def prime(n):
    if n<2:
        return False
    s=int(n**0.5)
    for i in range(2,s+1):
        if n%i==0:
            return False
    return True
n=int(input())
if prime(n):
    is_prime=1
else:
    is_prime=0
if is_prime==0:
    print("Not Mega Prime")
else:
    while n>0:
        r=n%10
        if not prime(r):
            print("Not Mega Prime")
            break
        n=n//10
    if n==0:
        print("Mega Prime")