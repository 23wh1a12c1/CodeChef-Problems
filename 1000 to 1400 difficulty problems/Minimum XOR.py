# cook your dish here
def min_xor_after_removal(arr):
    total_xor = 0
    for num in arr:
        total_xor ^= num

    min_xor = total_xor  # case when no element is removed
    for num in arr:
        min_xor = min(min_xor, total_xor ^ num)
    return min_xor

# Reading input efficiently
import sys
input = sys.stdin.read
data = input().split()

idx = 0
T = int(data[idx])
idx += 1

results = []
for _ in range(T):
    N = int(data[idx])
    idx += 1
    arr = list(map(int, data[idx:idx+N]))
    idx += N
    results.append(str(min_xor_after_removal(arr)))

print("\n".join(results))
