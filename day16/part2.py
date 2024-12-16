import heapq

lines = [l.strip() for l in open(0)]

for y, row in enumerate(lines):
    for x, cell in enumerate(row):
        if cell == "S":
            start = x, y, 1, 0
        if cell == "E":
            end = x, y

states = [(0, start, None)]

cost_of = {}
prev_tiles = {}

while states:
    cost, (x, y, dx, dy), prev = heapq.heappop(states)
    # print(cost, (x, y, dx, dy))
    first = (x, y, dx, dy) not in cost_of
    if first:
        cost_of[(x, y, dx, dy)] = cost
        prev_tiles[(x, y, dx, dy)] = set()
    if cost > cost_of[(x, y, dx, dy)]:
        continue
    prev_tiles[(x, y, dx, dy)].add(prev)

    if not first:
        continue

    new = [(cost + 1000, (x, y, -dy, dx)), (cost + 1000, (x, y, dy, -dx)), (cost + 1, (x + dx, y + dy, dx, dy))]
    for c, (x2, y2, dx2, dy2) in new:
        # print(lines[y][x])
        if lines[y][x] != "#":
            heapq.heappush(states, (c, (x2, y2, dx2, dy2), (x, y, dx, dy)))

#
min_cost = min(cost_of[st] for st in [(*end, 1, 0), (*end, -1, 0), (*end, 0, 1), (*end, 1, 0)])


print([cost_of[st] for st in [(*end, 1, 0), (*end, -1, 0), (*end, 0, 1), (*end, 1, 0)]])
print(min_cost)

current = { st for st in [(*end, 1, 0), (*end, -1, 0), (*end, 0, 1), (*end, 1, 0)] if cost_of[st] == min_cost }
print(current)

print([prev_tiles[s] for s in current])

seen = set()

while current:
    st = current.pop()
    seen.add((st[0], st[1]))
    for st2 in prev_tiles[st]:
        if st2 is not None:
            current.add(st2)

for y, row in enumerate(lines):
    for x, cell in enumerate(row):
        print("o" if (x, y) in seen else cell, end="")
    print()

print(len(seen))