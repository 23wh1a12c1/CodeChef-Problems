# PYTHON3


def count_groups(s):
    count = 0
    in_group = False
    for ch in s:
        if ch == '1':
            if not in_group:
                count += 1
                in_group = True
        else:
            in_group = False
    return count

# Input reading
T = int(input())
for _ in range(T):
    S = input().strip()
    print(count_groups(S))
