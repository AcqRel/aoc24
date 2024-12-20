lines = [l.strip() for l in open(0)]
lines = [l for l in lines if l]

w, h = len(lines[0]), len(lines)

walls = set()
for y in range(h):
    for x in range(w):
        if lines[y][x] == "S":
            sx, sy = x, y
        elif lines[y][x] == "E":
            ex, ey = x, y
        elif lines[y][x] == "#":
            walls.add((x, y))

dist = dict()

cx, cy = sx, sy
for d in range(w*h):
    print(".")
    dist[(cx, cy)] = d
    if (cx, cy) == (ex, ey):
        break
    
    for nx in [(cx - 1, cy), (cx + 1, cy), (cx, cy - 1), (cx, cy + 1)]:
        if nx not in dist and nx not in walls:
            cx, cy = nx
            break
    else:
        assert False

count = 0
for y in range(h):
    for x in range(w):
        # print(dist[(x, y)] if (x, y) in dist else "-")
        if (x, y - 1) in dist and (x, y + 1) in dist:
            if abs(dist[(x, y - 1)] - dist[(x, y + 1)]) - 2 >= 100:
                count += 1
        if (x - 1, y) in dist and (x + 1, y) in dist:
            if abs(dist[(x - 1, y)] - dist[(x + 1, y)]) - 2 >= 100:
                count += 1

print(count)
