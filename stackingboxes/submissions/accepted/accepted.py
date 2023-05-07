from sys import stdin 

def check_valid(i, j):
    return i % 2 == j % 2



n = int(stdin.readline())


rects = []

for _ in range(n):
    a, b = list(map(int, stdin.readline().split()))
    rects.append((a, b))

new_rects = []
for x, y in rects:
    new_rects.append((x, y))
    new_rects.append((y, x))

best_heights = [h for _, h in new_rects]

for i in range(2*n):
    b1, h1 = new_rects[i]
    for j in range(i + 1, 2*n):
        b2, h2 = new_rects[j]

        if b1 == h2 and b2 == h1 and not check_valid(i, j):
            continue

        if b2 <= b1:
            best_heights[j] = max(best_heights[j], best_heights[i] + h2)
        
print(max(best_heights))