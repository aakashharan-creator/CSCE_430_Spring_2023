from sys import stdin, exit

line = stdin.readline().strip().split()
print(line)
assert len(line) == 1, "one integer was not given"

n = line[0]

assert n.isdigit(), "%s is not an integer" % n

n = int(n)

assert (n >= 1 and n <= 1000), "%s, given n is not in the range 1 to 1000" % (n)

rects = stdin.readlines()

assert len(rects) == n, "expected %s rectangles, got %s" % (n, len(rects))
# print("RECTS: ", rects)
for line in rects:
    a, b = line.strip().split()
    assert a.isdigit() and b.isdigit(), "did not get integer for dimensions of rectangle"

    a = int(a)
    b = int(b)

    assert 1 <= a <= 200 and 1<= b <= 200, "dimensions of rectangle are not in range 1 to 200"

exit(42)