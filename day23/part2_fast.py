from collections import defaultdict

neighbours = defaultdict(set)
for l in open(0):
    a, b = sorted(l.strip().split("-"))
    neighbours[a].add(b)

cliques = [(n, m) for n in neighbours for m in neighbours[n]]

while True:
    new_cliques = [
        (*clique, n)
        for clique in cliques
        for n in neighbours[clique[-1]]
        if all(n in neighbours[m] for m in clique)
    ]
    if not new_cliques: break
    cliques = new_cliques

print(",".join(list(cliques)[0]))
