import sys
import bisect

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    events = []
    for i in range(n):
        s = int(next(it))
        e = int(next(it))
        events.append((s, e, i))  # (start, end, original_index)

    # Sort by start time
    starts = sorted((s, idx) for (s, _, idx) in events)
    start_times = [s for s, _ in starts]

    ans = [-1] * n
    for s, e, orig_idx in events:
        pos = bisect.bisect_left(start_times, e)
        if pos < n:
            ans[orig_idx] = starts[pos][1]
        else:
            ans[orig_idx] = -1

    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    solve()
