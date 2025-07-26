import math

T = int(input())
for _ in range(T):
    N, X = map(int, input().split())
    needed = max(0, N - X)
    packets = math.ceil(needed / 4)
    print(packets)
