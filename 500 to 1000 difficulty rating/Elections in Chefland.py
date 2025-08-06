# cook your dish here
t = int(input())
for _ in range(t):
    n, x = map(int,input().split())
    arr = list(map(int,input().split()))
    cnt = 0
    for i in arr:
        if i >= x:
            cnt += 1
    print(cnt)
        
