from collections import defaultdict

lines = [l.strip().split("-") for l in open(0)]

neighbours = defaultdict(set)
for a, b in lines:
    neighbours[a].add(b)
    neighbours[b].add(a)

cliques = set(map(tuple, lines))

while True:
    new_cliques = set()
    for cli in cliques:
        for n in neighbours[cli[0]]:
            if all(n in neighbours[m] for m in cli):
                new_cliques.add(tuple(sorted(cli + (n,))))
    if not new_cliques: break
    cliques = new_cliques

print(",".join(list(cliques)[0]))
