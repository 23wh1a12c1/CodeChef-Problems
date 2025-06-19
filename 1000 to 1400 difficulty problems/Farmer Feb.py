# cook your dish here
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    total = x + y
    z = 1
    while True:
        if is_prime(total + z):
            print(z)
            break
        z += 1
