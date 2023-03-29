from sys import stdin, exit

line = list(stdin.readline().strip().split())

assert len(line) == 2, "two integers were not given"

(n, k) = line

assert (n.isdigit() and k.isdigit()) and (int(n) > 0 and int(k) > 0), "%s, %s given n, k are not positive integers" % (n, k)

n = int(n)
k = int(k)

assert 1 <= n <= 100_000, "%s  not in [1, 100_000]" % (n)
assert 1 <= k <= 10_000, "%s  not in [1, 10_000]" % (k)

cars = stdin.readline().strip().split()

assert len(cars) == n, "num cars %s not equal to %s" % (len(cars), n)

for c in cars:
    assert c.lstrip("-").isdigit(), "%s is not an integer", c
    c = int(c)
    assert -1_000_000 <= c <= 1_000_000, "%s is not in the range [-1_000_000, 1_000_000]" % c

exit(42)