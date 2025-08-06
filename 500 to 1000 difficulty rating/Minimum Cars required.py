# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    if n % 4 == 0:
        print(n // 4)
    else:
        ans = n // 4 + 1
        print(ans)
