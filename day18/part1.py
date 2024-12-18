import re

ints = lambda s: list(map(int, re.findall(r"[+-]?\d+", s)))
lines = [ints(l) for l in open(0)]

walls = set()
for x, y in lines[:1024]:
    walls.add((x, y))

for i in range(71):
    walls.add((-1, i))
    walls.add((71, i))
    walls.add((i, -1))
    walls.add((i, 71))

curr = set([(0, 0)])
seen = set()

for dist in range(10**10):
    if (70, 70) in curr:
        print(dist)
        break
    new = set()
    for x, y in curr:
        for x2, y2 in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if (x2, y2) not in walls and (x2, y2) not in seen:
                new.add((x2, y2))
    curr = new
    seen |= new