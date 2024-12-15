import re

lines = open(0).read().strip()

lines, cmds = lines.split("\n\n")

walls = set()
boxes = set()

for y, line in enumerate(lines.split("\n")):
    for x, c in enumerate(line):
        if c == "@":
            rx, ry = x, y
        if c == "#":
            walls.add((x, y))
        if c == "O":
            boxes.add((x, y))

for c in cmds:
    if c not in "^v<>": continue

    if c == ">": dx, dy = 1, 0
    if c == "<": dx, dy = -1, 0
    if c == "v": dx, dy = 0, 1
    if c == "^": dx, dy = 0, -1
    px, py = rx + dx, ry + dy
    sx, sy = px, py
    while (px, py) in boxes: px, py = px + dx, py + dy
    if (px, py) in walls: continue
    if (px, py) != (sx, sy):
        boxes.remove((sx, sy))
        boxes.add((px, py))
    rx, ry = sx, sy


print(sum(x + y * 100 for x, y in boxes))
