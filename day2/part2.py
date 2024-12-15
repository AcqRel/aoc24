lines = [list(map(int, l.strip().split())) for l in open(0)]

num_safe = 0
for line in lines:
    for i in range(len(line)):
        short = line[:i] + line[i + 1:]
        diffs = [a - b for a, b in zip(short, short[1:])]
        if all(n in [1, 2, 3] for n in diffs) or all(n in [-1, -2, -3] for n in diffs):
            num_safe += 1
            break

print(num_safe)