def is_feasible(boards, k, max_len):
    total = 0
    painters = 1
    for length in boards:
        if total + length <= max_len:
            total += length
        else:
            painters += 1
            total = length
            if painters > k:
                return False
    return True

def painter_partition(boards, k):
    low = max(boards)            # At least one board must be painted fully
    high = sum(boards)           # One painter paints everything
    
    while low < high:
        mid = (low + high) // 2
        if is_feasible(boards, k, mid):
            high = mid
        else:
            low = mid + 1
    return low
def main():
    t = int(input())  
    for _ in range(t):
        N, k = map(int, input().split())
        boards = list(map(int, input().split()))
        print(painter_partition(boards, k))

if __name__ == "__main__":
    main()
