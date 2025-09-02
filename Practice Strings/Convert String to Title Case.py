T = int(input())

for _ in range(T):
    S = input()
    words = S.split()
    result = []
    for word in words:
        if word.isupper():
            # It's an acronym, keep as is
            result.append(word)
        else:
            # Convert to title case
            result.append(word.capitalize())
    print(" ".join(result))
