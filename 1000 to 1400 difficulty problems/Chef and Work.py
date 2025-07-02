def chef_and_work(test_cases):
    results = []
    for _ in range(test_cases):
        n, k = map(int, input().split())
        weights = list(map(int, input().split()))

        trips = 0
        current_load = 0
        possible = True

        for w in weights:
            if w > k:
                possible = False
                break
            if current_load + w > k:
                trips += 1
                current_load = w
            else:
                current_load += w
        
        if not possible:
            results.append(-1)
        else:
            if current_load > 0:
                trips += 1  # for last trip
            results.append(trips)
    
    for res in results:
        print(res)

# Sample usage
t = int(input())
chef_and_work(t)
