import re
lines = open(0).read()

print(sum(int(a) * int(b) for a, b in re.findall(r'mul\((\d+),(\d+)\)', lines)))
