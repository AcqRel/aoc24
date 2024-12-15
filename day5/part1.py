lines = open(0).read()

orderings, groups = lines.split("\n\n")
orderings = [list(map(int, g.split("|"))) for g in orderings.split()]
groups = [list(map(int, g.split(","))) for g in groups.split()]

total = 0
for group in groups:
    for a, b in orderings:
        try:
            if group.index(a) > group.index(b):
                break
        except ValueError:
            pass
    else:
        print(group)
        total += group[len(group) // 2]

print(total)