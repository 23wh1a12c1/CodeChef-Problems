# cook your dish here
T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    
    ops = 0
    for i in range(1, N):
        if S[i] == S[i - 1]:
            ops += 1
    print(ops)


