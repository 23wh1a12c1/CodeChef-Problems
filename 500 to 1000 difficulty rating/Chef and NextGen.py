T = int(input())
for _ in range(T):
    A, B, X, Y = map(int, input().split())
    if A * B <= X * Y:
        print("Yes")
    else:
        print("No")
