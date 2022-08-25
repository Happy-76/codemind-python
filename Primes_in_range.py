def is_prime(n):
    if n == 1:
        return False
    m = int(n ** 0.5) + 1
    for i in range(2, m):
        if n % i == 0:
            return False
    return True
    
a = int(input())
b = int(input())
cnt = 0
for i in range(a, b + 1):
    if is_prime(i):
        cnt += 1
print(cnt)