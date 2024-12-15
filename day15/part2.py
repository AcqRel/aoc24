import re

lines = open(0).read().strip()

lines, cmds = lines.split("\n\n")

walls = set()
boxes = set()

for y, line in enumerate(lines.split("\n")):
    for x, c in enumerate(line):
        if c == "@":
            rx, ry = x*2, y
        if c == "#":
            walls.add((x*2, y))
            walls.add((x*2+1, y))
        if c == "O":
            boxes.add((x*2, y))

for c in cmds:
    # for y in range(max(y for (x, y) in walls) + 1):
    #     for x in range(max(x for (x, y) in walls) + 1):
    #         ch = '#' if (x, y) in walls else \
    #             '[' if (x, y) in boxes else \
    #             ']' if (x-1, y) in boxes else \
    #             '@' if (x, y) == (rx, ry) else '.'
    #         print(ch, end="")
    #     print()
    # print()
    # print(c)
    
    if c == "<":
        nb = 0
        while (rx - (nb + 1) * 2, ry) in boxes: nb += 1
        if (rx - nb * 2 - 1, ry) in walls: continue
        for x in range(rx - nb*2, rx, 2): boxes.remove((x, ry))
        for x in range(rx - nb*2 - 1, rx - 1, 2): boxes.add((x, ry))
        rx -= 1
    if c == ">":
        nb = 0
        while (rx + nb * 2 + 1, ry) in boxes: nb += 1
        if (rx + nb * 2 + 1, ry) in walls: continue
        for x in range(rx + 1, rx + nb * 2 + 1, 2): boxes.remove((x, ry))
        for x in range(rx + 2, rx + nb * 2 + 2, 2): boxes.add((x, ry))
        rx += 1
    if c in "^v":
        dy = 1 if c == "v" else -1

        if (rx, ry + dy) in walls: continue
        
        stack = set()
        row = { (x, y) for (x, y) in [(rx - 1, ry + dy), (rx, ry + dy)] if (x, y) in boxes }
        while row:
            stack |= row
            new_row = {
                (x, y)
                for (bx, by) in row
                for (x, y) in [(bx - 1, by + dy), (bx, by + dy), (bx + 1, by + dy)]
                if (x, y) in boxes
            }
            row = new_row
        if any((x, y + dy) in walls or (x + 1, y + dy) in walls for (x, y) in stack):
            continue
        print(stack)
        for (x, y) in stack: boxes.remove((x, y))
        for (x, y) in stack: boxes.add((x, y + dy))
        ry += dy

for y in range(max(y for (x, y) in walls) + 1):
    for x in range(max(x for (x, y) in walls) + 1):
        ch = '#' if (x, y) in walls else \
            '[' if (x, y) in boxes else \
            ']' if (x-1, y) in boxes else \
            '@' if (x, y) == (rx, ry) else '.'
        print(ch, end="")
    print()
print()

print(sum(x + y * 100 for x, y in boxes))
