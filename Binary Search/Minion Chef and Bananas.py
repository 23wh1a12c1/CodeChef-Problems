import math

def min_eating_speed(piles, h):
    left, right = 1, max(piles)
    while left < right:
        mid = (left + right) // 2
        hours = sum((pile + mid - 1) // mid for pile in piles)
        if hours > h:
            left = mid + 1
        else:
            right = mid
    return left

t = int(input())
for _ in range(t):
    n, h = map(int, input().split())
    piles = list(map(int, input().split()))
    print(min_eating_speed(piles, h))
