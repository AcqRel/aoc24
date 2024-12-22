import re
from collections import defaultdict

ints = lambda s: list(map(int, re.findall(r"[+-]?\d+", s)))
lines = [ints(l) for l in open(0)]

total_for = defaultdict(lambda: 0)
for n, in lines:
    seq = [n % 10]
    for _ in range(2000):
        n ^= 16777215 & (n << 6)
        n ^= 16777215 & (n >> 5)
        n ^= 16777215 & (n << 11)
        seq.append(n % 10)

    diffs = [a - b for a, b in zip(seq[1:], seq)]
    best_for = defaultdict(lambda: 0)
    for i in range(len(diffs) - 3):
        hist = tuple(diffs[i:i+4])
        if hist not in best_for:
            best_for[hist] = seq[i + 4]

    for h, d in best_for.items():
        total_for[h] += d

print(max(total_for.values()))
