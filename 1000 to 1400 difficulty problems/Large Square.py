# cook your dish here
import math

def largest_mega_square_side(n, a):
    k = int(math.isqrt(n)) 
    return k * a

# Read input
T = int(input())
for _ in range(T):
    n, a = map(int, input().split())
    print(largest_mega_square_side(n, a))
