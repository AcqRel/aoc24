import re

ints = lambda s: list(map(int, re.findall(r"[+-]?\d+", s)))
lines = [ints(l) for l in open(0)]

(w, h), lines = lines[0], lines[1:]

ul, ur, dl, dr = 0, 0, 0, 0

for x, y, vx, vy in lines:
    x = (x + vx * 100) % w
    y = (y + vy * 100) % h
    mx = w // 2
    my = h // 2

    if x < mx and y < my: ul += 1
    if x > mx and y < my: ur += 1
    if x < mx and y > my: dl += 1
    if x > mx and y > my: dr += 1

print(ul * ur * dl * dr)