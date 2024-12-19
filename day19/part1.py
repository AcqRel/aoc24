lines = [l.strip() for l in open(0)]
lines = [l for l in lines if l]

avail = lines[0].split(", ")

total = 0
for target in lines[1:]:
    seen = set()
    curr = {target}

    while curr:
        pat = curr.pop()
        for part in avail:
            if pat.startswith(part):
                without = pat[len(part):]
                if without not in seen:
                    curr.add(without)
                    seen.add(without)
    

    if "" in seen:
        total += 1
print(total)