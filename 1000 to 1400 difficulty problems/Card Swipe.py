def max_people_in_office(test_cases):
    results = []
    for A in test_cases:
        current = set()
        max_people = 0
        for id in A:
            if id in current:
                current.remove(id)
            else:
                current.add(id)
                max_people = max(max_people, len(current))
        results.append(max_people)
    return results

# Input reading
T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    test_cases.append(A)

# Process and output results
answers = max_people_in_office(test_cases)
for ans in answers:
    print(ans)
