from collections import Counter

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    freq = Counter(A)
    
    max_count = max(freq.values())
    min_val = min(k for k, v in freq.items() if v == max_count)
    
    print(min_val, max_count)
