from collections import defaultdict

lines = [list(l.strip()) for l in open(0)]

by_chr = defaultdict(list)

w, h = len(lines[0]), len(lines)

for y, row in enumerate(lines):
    for x, ch in enumerate(row):
        if ch != '.':
            by_chr[ch] += [(x, y)]

antinodes = set()
for positions in by_chr.values():
    for pos1 in positions:
        for pos2 in positions:
            if pos1 == pos2: continue
            pos3 = (pos1[0] + (pos1[0] - pos2[0]), pos1[1] + (pos1[1] - pos2[1]))
            x, y = pos3
            if 0 <= x < w and 0 <= y < h:
                antinodes.add(pos3)


print(len(antinodes))