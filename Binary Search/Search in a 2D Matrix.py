def searchMatrix(matrix, target):
    N = len(matrix)
    M = len(matrix[0])
    
    # Initialize binary search bounds
    left, right = 0, N * M - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Map the 1D mid index to 2D matrix (row, column)
        mid_value = matrix[mid // M][mid % M]
        
        if mid_value == target:
            return "YES"
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return "NO"

# Read input
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
target = int(input())

# Call the function and print result
print(searchMatrix(matrix, target))
