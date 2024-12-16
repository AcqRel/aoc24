import heapq

lines = [l.strip() for l in open(0)]

for y, row in enumerate(lines):
    for x, cell in enumerate(row):
        if cell == "S":
            start = x, y, 1, 0
        if cell == "E":
            end = x, y

states = [(0, start)]
seen = set()

while True:
    cost, (x, y, dx, dy) = heapq.heappop(states)
    # print(cost, (x, y, dx, dy))
    if (x, y, dx, dy) in seen:
        continue
    seen.add((x, y, dx, dy))
    if (x, y) == end:
        print(cost)
        break
    
    new = [(cost + 1000, (x, y, -dy, dx)), (cost + 1000, (x, y, dy, -dx)), (cost + 1, (x + dx, y + dy, dx, dy))]
    for c, (x2, y2, dx2, dy2) in new:
        # print(lines[y][x])
        if lines[y][x] != "#":
            heapq.heappush(states, (c, (x2, y2, dx2, dy2)))


