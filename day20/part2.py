from collections import defaultdict

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

by_length = defaultdict(lambda: 0)

for y in range(h):
    # print(y)
    for x in range(w):
        if (x, y) not in dist: continue
        for y2 in range(y - 20, y + 21):
            for x2 in range(x - 20, x + 21):
                if abs(x - x2) + abs(y - y2) <= 20:
                    if (x, y) in dist and (x2, y2) in dist:
                        dist_before = dist[(x, y)] - dist[(x2, y2)]
                        dist_after = abs(x - x2) + abs(y - y2)
                        if dist_before - dist_after >= 100:
                            count += 1
                            by_length[dist_before - dist_after] += 1

for l in sorted(by_length):
    print(l, by_length[l])

print(count)
