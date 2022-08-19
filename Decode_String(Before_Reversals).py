t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    string = input()
    p=b
    for j in range(p):
        s = string[:b]
        string = s[::-1]+string[b:]
        b =b-1
    print(string)
        
        

        