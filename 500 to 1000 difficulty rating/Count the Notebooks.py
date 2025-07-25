T = int(input())  # Number of test cases

for _ in range(T):
    N = int(input())  # Weight of pulp in kgs
    notebooks = (N * 1000) // 100  # Total pages divided by pages per notebook
    print(notebooks)
