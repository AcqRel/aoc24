import random

vals = {}

lines = list(open(0))

seen_vars = set()

unordered = []
for line in lines:
    if ": " in line:
        seen_vars.add(line.split(": ")[0])
        continue
    parts = line.split()
    if not parts: continue
    unordered += [(parts[1], parts[0], parts[2], parts[4])]



def correct_for_n(n_bits, swaps):
    global unordered, gates

    mapping = {}
    for a, b in swaps:
        mapping[a] = b
        mapping[b] = a

    any_new = True
    gates = []
    seen_vars2 = set(seen_vars)
    while any_new:
        any_new = False

        for op, a, b, c in unordered:
            if a in seen_vars2 and b in seen_vars2 and mapping.get(c, c) not in seen_vars2:
                seen_vars2.add(mapping.get(c,c))
                gates += [(op, a, b, c)]
                any_new = True

    if len(gates) < len(unordered):
        return False

    unordered = gates

    for _ in range(100):
        vals = {}
        x = random.randint(0, 2**45)
        y = random.randint(0, 2**45)
        z = x + y

        for i in range(45):
            vals[f"x{i:02}"] = x & (1 << i) != 0
            vals[f"y{i:02}"] = y & (1 << i) != 0

        for op, a, b, c in gates:
            c = mapping.get(c, c)
            match op:
                case "OR": vals[c] = vals[a] or vals[b]
                case "XOR": vals[c] = vals[a] != vals[b]
                case "AND": vals[c] = vals[a] and vals[b]

        for i in range(n_bits):
            if vals[f"z{i:02}"] != (z & (1 << i) != 0):
                return False
    return True

num_correct = 0
swaps = []

possible_outs = [gate[3] for gate in unordered]

while num_correct < 46:

    if correct_for_n(num_correct + 1, swaps):
        print(num_correct, swaps)
        num_correct += 1
        continue

    swaps2 = swaps + [(random.choice(possible_outs), random.choice(possible_outs))]
    if correct_for_n(num_correct + 1, swaps2):
        swaps = swaps2
        continue

print(",".join(sorted(s for swap in swaps for s in swap)))
