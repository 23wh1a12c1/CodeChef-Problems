T = int(input())  # Number of test cases

for _ in range(T):
    N, X, Y = map(int, input().split())
    
    # Chef can only score X marks per correct answer, so:
    # Y must be divisible by X, and number of such X-marks <= N
    if Y % X == 0 and Y // X <= N:
        print("YES")
    else:
        print("NO")
