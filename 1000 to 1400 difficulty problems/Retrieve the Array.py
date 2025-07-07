t = int(input())
for _ in range(t):
    n = int(input())
    B = list(map(int, input().split()))
    
    total_B = sum(B)
    total_A = total_B // (n + 1)
    
    A = [b - total_A for b in B]
    print(*A)
