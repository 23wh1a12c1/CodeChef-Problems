t = int(input())

while t > 0:
    n = int(input())
    d = list(map(int, input().split()))
    
    ok = True
    for i in range(1, n):
        if d[i] < d[i-1]:
            ok = False
            break
    
    print("Yes" if ok else "No")
    t -= 1
