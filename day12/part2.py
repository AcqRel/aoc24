lines = [list(l.strip()) for l in open(0)]

all_cells = {(x, y): c for y, row in enumerate(lines) for x, c in enumerate(row)}
remaining_cells  = {(x, y): c for y, row in enumerate(lines) for x, c in enumerate(row)}

total = 0
while remaining_cells:
    print()
    pos = next(iter(remaining_cells))
    ch = all_cells[pos]

    area = 0
    fences = set()
    queue = [(None, pos)]
    while queue:
        prev, (x, y) = queue.pop()
        if all_cells.get((x, y), "") != ch:
            (x1, y1), (x2, y2) = prev, (x, y)
            fences.add(((x1, y1), (x2, y2)))
        elif remaining_cells.get((x, y)) == ch:
            area += 1
            del remaining_cells[(x, y)]
            queue += [((x, y), pos2) for pos2 in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))]
            # print(queue)


    sides = 0
    for (x1, y1), (x2, y2) in fences:
        print((x1, y1), (x2, y2))
        if y2 == y1 + 1 or y2 == y1 - 1:
            if ((x1 - 1, y1), (x2 - 1, y2)) not in fences:
                sides += 1
        elif x2 == x1 + 1 or x2 == x1 - 1:
            if ((x1, y1 - 1), (x2, y2 - 1)) not in fences:
                sides += 1
        else:
            assert False



    total += sides * area

print(total)
