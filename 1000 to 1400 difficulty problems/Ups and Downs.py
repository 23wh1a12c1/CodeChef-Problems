def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        A.sort()
        for i in range(1, N - 1, 2):
            A[i], A[i + 1] = A[i + 1], A[i]
        print(*A)

solve()
