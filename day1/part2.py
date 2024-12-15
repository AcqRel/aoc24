from collections import defaultdict

lines = [list(map(int, l.strip().split())) for l in open(0)]
left, right = list(zip(*lines))

count_in_r = defaultdict(int)
for n in right:
    count_in_r[n] += 1

print(sum(n * count_in_r[n] for n in left))

