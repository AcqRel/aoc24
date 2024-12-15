lines = [list(map(int, l.strip())) for l in open(0)]

targets = [[{(x, y)} if n == 9 else set() for x, n in enumerate(l)] for y, l in enumerate(lines)]

for n in reversed(range(9)):
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] != n: continue
            for x2, y2 in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= x2 < len(lines[0]) and 0 <= y2 < len(lines) and lines[y2][x2] == n + 1:
                    targets[y][x] |= targets[y2][x2]

print(sum(len(c) for y, row in enumerate(targets) for x, c in enumerate(row) if lines[y][x] == 0))
