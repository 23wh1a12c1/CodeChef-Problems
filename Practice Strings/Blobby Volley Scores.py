def blobby_volley_score(n, s):
    alice_score, bob_score = 0, 0
    server = 'A'  # Alice always starts as server

    for ch in s:
        if server == 'A':
            if ch == 'A':  # Alice is server and wins
                alice_score += 1
            else:          # Bob wins → becomes server
                server = 'B'
        else:  # server = 'B'
            if ch == 'B':  # Bob is server and wins
                bob_score += 1
            else:          # Alice wins → becomes server
                server = 'A'

    return alice_score, bob_score


# Main Driver
T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    S = input().strip()
    a, b = blobby_volley_score(N, S)
    print(a, b)
