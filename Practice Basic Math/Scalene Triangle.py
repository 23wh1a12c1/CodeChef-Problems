# Read number of test cases
T = int(input())

for _ in range(T):
    A, B, C = map(int, input().split())
    
    # Check if all sides are distinct
    if A != B and B != C and A != C:
        print("YES")
    else:
        print("NO")
