T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    min_wins = max(0, X - Y)
    print(min_wins)
