# cook your dish here
T = int(input())
for _ in range(T):
    N = input().strip()
    digit_sum = sum(int(digit) for digit in N)
    print(digit_sum)
