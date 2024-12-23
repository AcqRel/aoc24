from collections import defaultdict

lines = [l.strip().split("-") for l in open(0)]

neighbours = defaultdict(set)
for a, b in lines:
    neighbours[a].add(b)
    neighbours[b].add(a)

triplets = set()
for a in neighbours:
    for b in neighbours[a]:
        for c in neighbours[a] & neighbours[b]:
            triplets.add(tuple(sorted([a, b, c])))

print(sum(any(c.startswith("t") for c in t) for t in triplets))
