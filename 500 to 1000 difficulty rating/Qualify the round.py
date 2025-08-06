# cook your dish here
t = int(input())
for _ in range(t):
    x, a, b = map(int, input().split())
    if a*1 + b*2 >= x:
        print("Qualify")
    else:
        print("NotQualify")
