import re
lines = open(0).read()

enabled = True
total = 0
for a, b, do, dont in re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", lines):
    if do:
        enabled = True
    if dont:
        enabled = False
    if a and b and enabled:
        total += int(a) * int(b)
print(total)
