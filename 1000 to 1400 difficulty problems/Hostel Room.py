T = int(input()) 

for _ in range(T):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    
    current = X
    max_people = X
    
    for change in A:
        current += change
        max_people = max(max_people, current)
    
    print(max_people)
