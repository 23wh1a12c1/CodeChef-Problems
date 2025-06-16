# cook your dish here
t = int(input())
for _ in range(t):
    X1, Y1, X2, Y2 = map(int, input().split())
    print("Yes" if (X1 + Y1 + X2 + Y2) % 2 == 0 else "No")
