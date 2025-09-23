#####    PYTHON3



def max_complete_layers(N):
    # We want to find the largest k such that sum of first k layers <= N
    # sum of first k natural numbers = k * (k + 1) // 2
    # So, find max k where k*(k+1)//2 <= N

    left, right = 0, N
    while left <= right:
        mid = (left + right) // 2
        total_bricks = mid * (mid + 1) // 2

        if total_bricks == N:
            return mid
        elif total_bricks < N:
            left = mid + 1
        else:
            right = mid - 1
    return right


T = int(input())
for _ in range(T):
    N = int(input())
    print(max_complete_layers(N))




