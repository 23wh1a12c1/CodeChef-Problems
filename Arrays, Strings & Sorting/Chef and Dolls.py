# cook your dish here

t =  int(input())
for _ in range(t):
    n = int(input())
    result = 0
    
    for i in range(n):
        a = int(input())
        result ^= a    # xor removes pairs
    print(result)    
