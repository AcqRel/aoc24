import re

ints = lambda s: list(map(int, re.findall(r"[+-]?\d+", s)))
lines = [ints(l) for l in open("input.txt")]

(w, h), lines = lines[0], lines[1:]

for n in range(38, 10**10, 101):

    count = [[0] * w for _ in range(h)]

    xs, ys = [], []

    for x, y, vx, vy in lines:
        x = (x + vx * n) % w
        y = (y + vy * n) % h
        count[y][x] += 1
        xs += [x]
        ys += [y]
    
    # sc = (max(xs) - min(xs)) * (max(ys) - min(ys))
    
    # if sc < 10200: # seems to repeat every 101 iterations starting at 38
    #     print(n, sc)

    for y in range(h):
        for x in range(w):
            print("#" if count[y][x] else ".", end="")
        print()

    input(f"iter {n}")
