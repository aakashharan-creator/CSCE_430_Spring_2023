from sys import stdin, setrecursionlimit

setrecursionlimit(10**9)

MAX_BASE = 250

def dfs_solve(prev_base, i, curr_height):
    if i == n:
        return curr_height

    curr_a, curr_b = rects[i]

    max_so_far = curr_height
    if curr_a <= prev_base:
        max_so_far = max(max_so_far, dfs_solve(curr_a, i + 1, curr_height + curr_b))
    
    if curr_b <= prev_base:
        max_so_far = max(max_so_far, dfs_solve(curr_b, i + 1, curr_height + curr_a))
    
    max_so_far = max(max_so_far, dfs_solve(prev_base, i + 1, curr_height))

    return max_so_far

n = int(stdin.readline())
rects = []

for _ in range(n):
    a, b = list(map(int, stdin.readline().split()))
    rects.append((a, b))

ans = dfs_solve(MAX_BASE, 0, 0)
print(ans)