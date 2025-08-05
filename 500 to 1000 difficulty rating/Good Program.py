T = int(input())  # Number of test cases

for _ in range(T):
    N = int(input())  # Number of bits used by the program
    if N % 4 == 0:
        print("Good")
    else:
        print("Not Good")
