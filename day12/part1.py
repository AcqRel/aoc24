lines = [list(l.strip()) for l in open(0)]

all_cells = {(x, y): c for y, row in enumerate(lines) for x, c in enumerate(row)}
remaining_cells  = {(x, y): c for y, row in enumerate(lines) for x, c in enumerate(row)}

total = 0
while remaining_cells:
    pos = next(iter(remaining_cells))
    ch = all_cells[pos]

    area = 0
    perim = 0
    queue = [pos]
    while queue:
        x, y = queue.pop()
        if all_cells.get((x, y), "") != ch:
            perim += 1
        elif remaining_cells.get((x, y)) == ch:
            area += 1
            del remaining_cells[(x, y)]
            queue += [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

    total += perim * area

print(total)
