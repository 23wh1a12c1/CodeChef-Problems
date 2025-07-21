T = int(input())  # Number of test cases

for _ in range(T):
    R = list(map(int, input().split()))  # Read 4 integers

    # If all decisions are 0 (inside), print IN
    if all(r == 0 for r in R):
        print("IN")
    else:
        print("OUT")
