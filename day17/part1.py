import re

ints = lambda s: list(map(int, re.findall(r"[+-]?\d+", s)))
lines = [ints(l.strip()) for l in open(0)]

a, b, c = [l[0] for l in lines[:3]]
nums = lines[4]

# print(a,b,c,nums)

pc = 0
while pc < len(nums):
    def comb():
        global pc
        v = nums[pc]
        pc += 1
        if v < 4: return v
        if v == 4: return a
        if v == 5: return b
        if v == 6: return c
        assert False
    def lit():
        global pc
        v = nums[pc]
        pc += 1
        return v

    if nums[pc] == 0:
        pc += 1
        a >>= comb()
    elif nums[pc] == 1:
        pc += 1
        b ^= lit()
    elif nums[pc] == 2:
        pc += 1
        b = comb() % 8
    elif nums[pc] == 3:
        pc += 1
        dst = lit()
        if a: pc = dst
    elif nums[pc] == 4:
        pc += 1
        lit()
        b ^= c
    elif nums[pc] == 5:
        pc += 1
        print(comb() % 8)
    elif nums[pc] == 6:
        pc += 1
        b = a >> comb()
    elif nums[pc] == 7:
        pc += 1
        c = a >> comb()

