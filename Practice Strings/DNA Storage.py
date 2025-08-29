# DNA Storage Problem

t = int(input())   # number of test cases

# Mapping for 2-bit to DNA character
mapping = {
    "00": "A",
    "01": "T",
    "10": "C",
    "11": "G"
}

while t > 0:
    n = int(input())   # length of binary string (even)
    s = input().strip()

    result = ""
    for i in range(0, n, 2):  # take 2 bits at a time
        pair = s[i:i+2]
        result += mapping[pair]

    print(result)
    t -= 1
