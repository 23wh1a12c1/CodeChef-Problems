def count_positive_products(test_cases):
    results = []
    for A in test_cases:
        pos = sum(1 for x in A if x > 0)
        neg = sum(1 for x in A if x < 0)
        # Pairs of positive numbers + pairs of negative numbers
        count = (pos * (pos - 1)) // 2 + (neg * (neg - 1)) // 2
        results.append(count)
    return results

# Input
T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    test_cases.append(A)

# Output
for res in count_positive_products(test_cases):
    print(res)
