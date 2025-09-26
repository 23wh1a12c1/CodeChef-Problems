def min_sprinkler_radius(houses, sprinklers):
    """
    Calculates the minimum radius required for sprinklers to protect all houses.

    Args:
        houses: A list of integers representing house positions.
        sprinklers: A list of integers representing sprinkler positions.

    Returns:
        The minimum radius as an integer.
    """
    houses.sort()
    sprinklers.sort()

    min_radius = 0
    sprinkler_index = 0

    for house_pos in houses:
        current_min_dist = float('inf')
        
        # Find the closest sprinkler for the current house
        while sprinkler_index < len(sprinklers) and sprinklers[sprinkler_index] < house_pos:
            sprinkler_index += 1
        
        # Consider the sprinkler just found (if it exists)
        if sprinkler_index < len(sprinklers):
            dist1 = abs(house_pos - sprinklers[sprinkler_index])
            current_min_dist = min(current_min_dist, dist1)
        
        # Consider the previous sprinkler (if it exists)
        if sprinkler_index > 0:
            dist2 = abs(house_pos - sprinklers[sprinkler_index - 1])
            current_min_dist = min(current_min_dist, dist2)
        
        # Update the overall minimum radius
        min_radius = max(min_radius, current_min_dist)

    return min_radius

# Read input
try:
    n = int(input())
    houses = list(map(int, input().split()))
    m = int(input())
    sprinklers = list(map(int, input().split()))

    # Calculate and print the result
    result = min_sprinkler_radius(houses, sprinklers)
    print(result)

except (IOError, ValueError):
    pass
