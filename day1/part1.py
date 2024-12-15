
lines = [list(map(int, l.strip().split())) for l in open(0)]
left, right = list(zip(*lines))
left, right = map(sorted, [left, right])
print(sum(abs(a - b) for a, b in zip(left, right)))
