T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    
    val1 = A * 10   # 10% -> multiply by 10
    val2 = B * 5    # 20% -> multiply by 5
    
    if val1 > val2:
        print("FIRST")
    elif val2 > val1:
        print("SECOND")
    else:
        print("ANY")
