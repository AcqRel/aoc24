lines = [list(map(int, l.strip().split())) for l in open(0)]

diffs = [[a - b for a, b in zip(line, line[1:])] for line in lines]
safe = [all(n in [1, 2, 3] for n in line) or all(n in [-1, -2, -3] for n in line) for line in diffs]
print(sum(safe))
