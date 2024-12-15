lines = [list(l.strip()) for l in open(0)]

for y2, line in enumerate(lines):
    for x2, c in enumerate(line):
        if c == "^": dx, dy = (0, -1) 
        elif c == "<": dx, dy = (-1, 0)
        elif c == ">": dx, dy = (1, 0)
        elif c == "v": dx, dy = (0, 1)
        else: continue
        x, y = x2, y2
        break

# This takes about two minutes on my slow computer but saves more than two
# minutes of thinking
obst = 0
st = (x, y, dx, dy)
for ob_y in range(len(lines)):
    print(ob_y)
    for ob_x in range(len(lines)):
        x, y, dx, dy = st
        visited_dirs = set()
        while True:
            if (x, y, dx, dy) in visited_dirs:
                obst += 1
                break
            visited_dirs.add((x, y, dx, dy))
            x += dx
            y += dy
            if not (0 <= x < len(lines[0]) and 0 <= y < len(lines)):
                break
            elif lines[y][x] == '#' or (x, y) == (ob_x, ob_y):
                x -= dx
                y -= dy
                dx, dy = -dy, dx

print(obst)

