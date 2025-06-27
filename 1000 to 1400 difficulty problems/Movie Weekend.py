# cook your dish here
T = int(input())

for _ in range(T):
    n = int(input())
    L = list(map(int, input().split()))
    R = list(map(int, input().split()))
    
    best_index = 0
    best_value = L[0] * R[0]
    best_rating = R[0]

    for i in range(1, n):
        product = L[i] * R[i]
        if product > best_value:
            best_value = product
            best_rating = R[i]
            best_index = i
        elif product == best_value:
            if R[i] > best_rating:
                best_rating = R[i]
                best_index = i
            elif R[i] == best_rating:
                continue

    print(best_index + 1)  
