import re

keys = []
locks = []

for schem in open(0).read().split("\n\n"):
    lines = schem.strip().split()
    heights = [sum(l[i] == "#" for l in lines) - 1 for i in range(len(lines[0]))]
    if "." in lines[0]:
        keys += [heights]
    else:
        locks += [heights]

print(keys, locks)

total = 0
for key in keys:
    for lock in locks:
        if all(a + b <= 5 for a, b in zip(key, lock)):
            total += 1
print(total)
