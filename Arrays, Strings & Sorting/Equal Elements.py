from collections import Counter

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    if n == 0:
        print(0)
        return

    # Count frequencies of each element
    counts = Counter(a)

    # Find the maximum frequency
    max_freq = 0
    if counts: # Handle empty array case for safety, though N >= 1 in constraints
        max_freq = max(counts.values())

    # The number of operations is N - max_freq
    print(n - max_freq)

# Read the number of test cases
t = int(input())
for _ in range(t):
    solve()
