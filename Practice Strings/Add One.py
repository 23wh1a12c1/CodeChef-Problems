# cook your dish here
def add_one(num_str: str) -> str:
    # Convert string to list of digits for easy manipulation
    digits = list(num_str)
    n = len(digits)

    carry = 1  # we are adding 1
    for i in range(n - 1, -1, -1):
        d = int(digits[i]) + carry
        digits[i] = str(d % 10)
        carry = d // 10
    
    if carry > 0:
        digits.insert(0, str(carry))
    
    return "".join(digits)


# Main driver
T = int(input().strip())
for _ in range(T):
    N = input().strip()
    print(add_one(N))
