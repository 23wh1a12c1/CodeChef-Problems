t = int(input())

while t > 0:
    x, y = map(int, input().split())
    # Your code goes here
    if y <= x:
        print(y)
    else:
        extra = y - x
        print(x + extra * 2)
    t -= 1
