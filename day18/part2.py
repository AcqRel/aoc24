import re

ints = lambda s: list(map(int, re.findall(r"[+-]?\d+", s)))
lines = [ints(l) for l in open(0)]

walls = set()

sz = max(n + 1 for l in lines for n in l)

def possible_with(n):
    walls = set()
    for x, y in lines[:n]:
        walls.add((x, y))

    for i in range(sz):
        walls.add((-1, i))
        walls.add((sz, i))
        walls.add((i, -1))
        walls.add((i, sz))

    curr = set([(0, 0)])
    seen = set()

    while curr:
        if (sz-1, sz-1) in curr:
            return True
        new = set()
        for x, y in curr:
            for x2, y2 in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if (x2, y2) not in walls and (x2, y2) not in seen:
                    new.add((x2, y2))
        curr = new
        seen |= new
    return False

for n in reversed(range(len(lines))):
    if possible_with(n):
        print(",".join(map(str,lines[n])))
        break

