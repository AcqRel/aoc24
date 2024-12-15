lines = [list(l.strip()) for l in open(0)]

count = 0
for y in range(len(lines) - 2):
    for x in range(len(lines[0]) - 2):
        if lines[x + 1][y + 1] != "A":
            continue
        if (lines[x][y], lines[x + 2][y + 2]) not in (("M", "S"), ("S", "M")):
            continue
        if (lines[x][y + 2], lines[x + 2][y]) not in (("M", "S"), ("S", "M")):
            continue
        count += 1
        
print(count)
