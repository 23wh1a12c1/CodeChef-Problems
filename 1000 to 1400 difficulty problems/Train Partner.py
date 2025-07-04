def find_partner_berth(n):
    pos_in_block = (n - 1) % 8 + 1

    # Mapping of position in block to (offset, type)
    partner_map = {
        1: (3, "LB"),  2: (3, "MB"),  3: (3, "UB"),
        4: (-3, "LB"), 5: (-3, "MB"), 6: (-3, "UB"),
        7: (1, "SU"),  8: (-1, "SL")
    }

    offset, berth_type = partner_map[pos_in_block]
    partner_berth = n + offset

    return f"{partner_berth}{berth_type}"

# Driver code
T = int(input())
for _ in range(T):
    N = int(input())
    print(find_partner_berth(N))
