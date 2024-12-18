import re, time

start = time.time()

walls = list(map(int, re.findall("[0-9]+", open(0).read())))
size = max(walls) + 2
walls = list(zip(walls[::2], walls[1::2]))

grid = [[0] * size for _ in range(size)]

for i in range(size):
    grid[i][size-1] = 1
    grid[size-1][i] = 1
for x, y in walls:
    grid[y][x] = 1

for i in reversed(range(len(walls) + 1)):
    try:
        x, y = walls[i]
        grid[y][x] = 0

        if not any(grid[y][x] == 2 for x, y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]):
            continue
    except IndexError:
        x, y = 0, 0

    queue = [(x, y)]
    while queue:
        x, y = queue.pop()
        if grid[y][x]: continue
        grid[y][x] = 2
        queue += [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

    if grid[size-2][size-2] == 2:
        print(*walls[i], sep=",")
        break

done = time.time()
print(f"{done - start:.4} s")
