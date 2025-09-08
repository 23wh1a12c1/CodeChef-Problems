# cook your dish here
# Read input values
N, X = map(int, input().split())
A = list(map(int, input().split()))

# Check if X is in A
if X in A:
    print("YES")
else:
    print("NO")
