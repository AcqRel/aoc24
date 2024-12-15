from collections import defaultdict

lines = open(0).read()

orderings, groups = lines.split("\n\n")
orderings = [list(map(int, g.split("|"))) for g in orderings.split()]
groups = [list(map(int, g.split(","))) for g in groups.split()]

preds = defaultdict(list)
for a, b in orderings:
    preds[b].append(a)


total = 0
for group in groups:
    ordered = []

    for a, b in orderings:
        try:
            if group.index(a) > group.index(b):
                break
        except ValueError:
            pass
    else:
        continue

    while len(ordered) < len(group):
        for n in group:
            if n not in ordered and all(p in ordered or p not in group for p in preds[n]):
                ordered.append(n)

    print(ordered)
    total += ordered[len(group) // 2]

print(total)
