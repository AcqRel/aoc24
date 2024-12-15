line = open(0).read().strip()

data = []
for i, c in enumerate(line):
    data += [i // 2 if i % 2 == 0 else -1] * int(c)

i = 0
j = len(data) - 1

while i < j:
    if data[i] != -1: i += 1; continue
    if data[j] == -1: j -= 1; continue
    data[i], data[j] = data[j], data[i]

print(sum(i * n for i, n in enumerate(data) if n >= 0))
