line = open(0).read().strip()

data = []
for i, c in enumerate(line):
    data += [i // 2 if i % 2 == 0 else -1] * int(c)

search_i = len(data) - 1
place_i = [0] * 10

t = 0

while search_i >= 0:
    if data[search_i] == -1:
        search_i -= 1
        continue
    
    l = 0
    while data[search_i - l] == data[search_i]:
        l += 1
    i = search_i - l + 1
    search_i -= l

    pi = place_i[l]
    while not all(n == -1 for n in data[pi:pi+l]) and pi < i:
        pi += 1
    if pi >= i:
        continue
    place_i[l] = pi

    n = data[i]

    for k in range(l):
        data[i + k] = -1
        data[pi + k] = n

print(sum(i * n for i, n in enumerate(data) if n >= 0))
