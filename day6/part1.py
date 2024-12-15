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

visited = set()
while True:
    visited.add((x, y))
    x += dx
    y += dy
    if not (0 <= x < len(lines[0]) and 0 <= y < len(lines)):
        break
    elif lines[y][x] == '#':
        x -= dx
        y -= dy
        dx, dy = -dy, dx

print(len(visited))
