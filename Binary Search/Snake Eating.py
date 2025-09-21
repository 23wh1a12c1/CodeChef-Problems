import sys
import bisect

input = sys.stdin.readline

def max_snakes_at_least_k(lengths, prefix_sum, N, K):
    # Find first index where length >= K
    idx = bisect.bisect_left(lengths, K)
    count_at_least_k = N - idx  # snakes already >= K
    
    # Binary search to find how many snakes below idx can be used to feed
    low, high = 0, idx
    res = 0
    while low <= high:
        mid = (low + high) // 2
        # Number of snakes to feed = idx - mid
        # Total length needed to upgrade all these to length K
        needed = K * (idx - mid) - (prefix_sum[idx] - prefix_sum[mid])
        if needed <= mid:  # we have enough snakes to feed (each snake eaten provides +1 length)
            res = idx - mid  # number of snakes that can be upgraded
            high = mid - 1
        else:
            low = mid + 1
    return count_at_least_k + res

T = int(input())
for _ in range(T):
    N, Q = map(int, input().split())
    lengths = list(map(int, input().split()))
    lengths.sort()
    prefix_sum = [0]
    for length in lengths:
        prefix_sum.append(prefix_sum[-1] + length)
    for __ in range(Q):
        K = int(input())
        print(max_snakes_at_least_k(lengths, prefix_sum, N, K))
