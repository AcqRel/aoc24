vals = {}

lines = list(open(0))

any_new = True
while any_new:
    any_new = False
    for line in lines:
        if ": " in line:
            name, val = line.strip().split(": ")
            if name not in vals:
                any_new = True
                vals[name] = (val == "1") 
        else:
            parts = line.split()
            if not parts: continue
            lhs = parts[0]
            rhs = parts[2]
            dst = parts[4]
            if lhs in vals and rhs in vals and dst not in vals:
                any_new = True
                match parts[1]:
                    case "OR": vals[dst] = vals[lhs] or vals[rhs]
                    case "XOR": vals[dst] = vals[lhs] != vals[rhs]
                    case "AND": vals[dst] = vals[lhs] and vals[rhs]


bits = []
for v in sorted(vals):
    if v.startswith("z"):
        bits += [vals[v]]

print(sum(n << i for i, n in enumerate(bits)))
