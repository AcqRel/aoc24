lines = [l.strip() for l in open(0)]

total = 0
for line in lines:
    output, inputs = line.split(": ")
    nrs = list(map(int, inputs.split()))

    assert output != 0

    targets = {int(output)}
    for n in reversed(nrs[1:]):
        new_nrs = set(k - n for k in targets if n <= k)
        new_nrs |= set(k // n for k in targets if n and k % n == 0)
        targets = new_nrs

    if nrs[0] in targets:
        total += int(output)
print(total)