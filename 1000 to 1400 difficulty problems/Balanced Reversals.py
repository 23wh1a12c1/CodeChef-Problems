# cook your dish here
T = int(input())
for _ in range(T):
    N = int(input())
    A = input().strip()
    count_0 = A.count('0')
    count_1 = N - count_0
    print('0' * count_0 + '1' * count_1)
