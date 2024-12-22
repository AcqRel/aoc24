import re

ints = lambda s: list(map(int, re.findall(r"[+-]?\d+", s)))
lines = [ints(l) for l in open(0)]

t = 0
for n, in lines:
    for _ in range(2000):
        n ^= 16777215 & (n << 6)
        n ^= 16777215 & (n >> 5)
        n ^= 16777215 & (n << 11)
    t += n

print(t)
