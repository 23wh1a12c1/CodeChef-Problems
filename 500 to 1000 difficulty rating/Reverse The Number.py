# cook your dish here
T = int(input())
for _ in range(T):
    N = input().strip()
    print(N[::-1].lstrip('0') or '0')
