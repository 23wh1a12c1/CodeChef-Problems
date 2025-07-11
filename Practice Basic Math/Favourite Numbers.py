def who_takes(A):
    if A % 2 == 0 and A % 7 == 0:
        return "Alice"
    if A % 2 == 1 and A % 9 == 0:
        return "Bob"
    return "Charlie"

def main():
    import sys
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    ans = []
    for i in range(1, t+1):
        A = int(data[i])
        ans.append(who_takes(A))
    print("\n".join(ans))

if __name__ == "__main__":
    main()
