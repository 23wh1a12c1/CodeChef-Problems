def kthSmallest(matrix, k):
    n = len(matrix)
    low, high = matrix[0][0], matrix[n-1][n-1]

    def countLessEqual(x):
        count, j = 0, n - 1
        for i in range(n):
            while j >= 0 and matrix[i][j] > x:
                j -= 1
            count += (j + 1)
        return count

    while low < high:
        mid = (low + high) // 2
        if countLessEqual(mid) < k:
            low = mid + 1
        else:
            high = mid
    return low

# Input Handling
N, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
print(kthSmallest(matrix, k))
