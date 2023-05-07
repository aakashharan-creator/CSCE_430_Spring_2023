from random import randint 

def check_valid(i, j):
    return i % 2 == j % 2

def solve(input_file, output_file):
    lines = None
    
    with open(input_file, "r") as file:
        lines = file.readlines()
    
    n = int(lines[0])
    rects = []

    for line in lines[1:]:
        a, b = list(map(int, line.split()))
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
            
    with open(output_file, 'w') as output:
        output.write(f"{max(best_heights)}\n")

n = 1000
l_lim = 1
u_lim = 150

for i in range(3):
    in_name = f"large{i}.in"
    out_name = f"large{i}.out"

    with open(in_name, "w") as input_file:
        input_file.write(f"{n}\n")

        for _ in range(n):
            a = randint(l_lim, u_lim + 1)
            b = randint(l_lim, u_lim + 1)

            input_file.write(f"{a} {b}\n")

    solve(in_name, out_name)
from random import randint 

def check_valid(i, j):
    return i % 2 == j % 2

def solve(input_file, output_file):
    lines = None
    
    with open(input_file, "r") as file:
        lines = file.readlines()
    
    n = int(lines[0])
    rects = []

    for line in lines[1:]:
        a, b = list(map(int, line.split()))
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
            
    with open(output_file, 'w') as output:
        output.write(f"{max(best_heights)}\n")

n = 1000
l_lim = 1
u_lim = 150

for i in range(3):
    in_name = f"large{i}.in"
    out_name = f"large{i}.ans"

    with open(in_name, "w") as input_file:
        input_file.write(f"{n}\n")

        for _ in range(n):
            a = randint(l_lim, u_lim + 1)
            b = randint(l_lim, u_lim + 1)

            input_file.write(f"{a} {b}\n")

    solve(in_name, out_name)
