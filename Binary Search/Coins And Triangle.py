import math

t = int(input())
for _ in range(t):
    n = int(input())
    h = int((math.isqrt(1 + 8*n) - 1) // 2)  # use integer sqrt
    print(h)
