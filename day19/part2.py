import heapq

lines = [l.strip() for l in open(0)]
lines = [l for l in lines if l]

avail = lines[0].split(", ")

total = 0
for target in lines[1:]:
    ways = {target: 1}

    curr = [(-len(target), target)]

    while curr:
        _, pat = heapq.heappop(curr)
        for part in avail:
            if pat.startswith(part):
                without = pat[len(part):]

                if without not in ways:
                    ways[without] = 0
                    heapq.heappush(curr, (-len(without), without))
                ways[without] += ways[pat]

    if "" in ways:
        total += ways[""]
print(total)