def solve():
    t = int(input().strip())
    for _ in range(t):
        X = int(input().strip())
        results = input().strip()

        # Calculate points
        carlsen_points = results.count('C') * 2 + results.count('D')
        chef_points = results.count('N') * 2 + results.count('D')

        # Decide prize
        if carlsen_points > chef_points:
            print(60 * X)
        elif chef_points > carlsen_points:
            print(40 * X)
        else:
            # tie case, Carlsen wins with reduced prize
            print(55 * X)

# Run the function
if __name__ == "__main__":
    solve()
