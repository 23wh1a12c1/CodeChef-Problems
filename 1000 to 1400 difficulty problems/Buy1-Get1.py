import math

try:
    T = int(input())
    for _ in range(T):
        s = input().strip()
        colors = [0] * 52  # 0-25 for 'A'-'Z', 26-51 for 'a'-'z'

        for c in s:
            if 'A' <= c <= 'Z':
                colors[ord(c) - ord('A')] += 1
            elif 'a' <= c <= 'z':
                colors[ord(c) - ord('a') + 26] += 1

        jewel = 0
        for count in colors:
            jewel += (count + 1) // 2  # same as ceil(count / 2) but integer safe

        print(jewel)

except Exception as e:
    print("Runtime Error:", e)
