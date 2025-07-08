import heapq

def min_operations_to_permutation(A, N):
    from collections import Counter
    freq = Counter(A)

    missing = []
    for i in range(1, N + 1):
        if freq[i] == 0:
            heapq.heappush(missing, i)

    operations = 0

    # Sort keys so we handle bigger (more costly to fix) elements first
    for num in sorted(freq.keys()):
        count = freq[num]
        if num > N or count > 1 or num < 1:
            extra = count - 1 if 1 <= num <= N else count
            for _ in range(extra):
                if not missing:
                    return -1
                need = heapq.heappop(missing)
                if need < num:
                    return -1
                operations += need - num

    return operations


# Driver code
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    print(min_operations_to_permutation(A, N))
