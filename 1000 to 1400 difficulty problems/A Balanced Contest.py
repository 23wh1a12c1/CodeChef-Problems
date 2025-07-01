T = int(input())
for _ in range(T):
    N, P = map(int, input().split())
    solves = list(map(int, input().split()))

    cakewalks = 0
    hards = 0

    for s in solves:
        if s >= P // 2:
            cakewalks += 1
        if s <= P // 10:
            hards += 1

    if cakewalks == 1 and hards == 2:
        print("yes")
    else:
        print("no")
