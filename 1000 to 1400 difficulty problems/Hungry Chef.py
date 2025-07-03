def hungry_chef():
    T = int(input())
    for _ in range(T):
        X, Y, N, R = map(int, input().split())

        # Case 1: Even all burgers as normal is too expensive
        min_cost = X * N
        if min_cost > R:
            print(-1)
            continue

        # Case 2: All premium burgers can be afforded
        max_cost = Y * N
        if max_cost <= R:
            print(0, N)
            continue

        # Greedy approach: maximize number of premium burgers
        # Let p = number of premium burgers, then:
        # n = N - p = number of normal burgers
        # Total cost = p * Y + (N - p) * X <= R
        # => p <= (R - N*X) // (Y - X)
        max_premium = (R - N * X) // (Y - X)
        p = min(N, max_premium)
        print(N - p, p)

# Run the function
hungry_chef()
