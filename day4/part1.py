lines = [list(l.strip()) for l in open(0)]

count = 0
for y in range(len(lines)):
    for x in range(len(lines[0])):
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if 0 <= x + 3 * dx < len(lines[0]) and 0 <= y + 3 * dy < len(lines):
                    for i, c in enumerate("XMAS"):
                        if lines[y + dy * i][x + dx * i] != c:
                            break
                    else:
                        count += 1

print(count)
