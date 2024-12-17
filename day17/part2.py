
def transpiled(a):

    b, c = 0, 0

    out = []
    while a:
        b = a % 8 # 2,4
        b = b ^ 1 # 1,1
        c = a >> b # 7,5
        b = b ^ 5 # 1,5
        b = b ^ c # 4,5
        a = a >> 3 # 0,3
        out += [b % 8] # 5,5
        pass # 3,0

    return out


def rewritten(a):

    out = []
    while a:
        b = (a % 8) ^ 1
        out += [(b ^ (a >> b) ^ 5) % 8] # 5,5
        a = a >> 3 # 0,3
        pass # 3,0

    return out


def with_z3():
    from z3 import Int, BitVec, solve

    a = BitVec("a", 128)
    
    exp = [2,4,1,1,7,5,1,5,4,5,0,3,5,5,3,0]
    constrs = []
    for i in range(16):
        sh = i * 3
        constrs += [(((a >> sh) % 8) ^ 1 ^ ((a >> sh) >> (((a >> sh) % 8) ^ 1)) ^ 5) % 8 == exp[i]]
    constrs += [a < 8 ** 16]
    print(z3.solve(constrs))

# with_z3()

def fast_search():
    with open("input.txt") as f:
        src = f.read()
    nums = list(map(int, src.strip().split()[-1].split(",")))

    def interpret(a):
        pc, b, c = 0, 0, 0
        out, out_sh = 0, 0
        while pc < len(nums):
            def comb():
                nonlocal pc
                v = nums[pc]
                pc += 1
                if v < 4: return v
                if v == 4: return a
                if v == 5: return b
                if v == 6: return c
                assert False
            def lit():
                nonlocal pc
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
                out += (comb() % 8) << out_sh
                out_sh += 3
            elif nums[pc] == 6:
                pc += 1
                b = a >> comb()
            elif nums[pc] == 7:
                pc += 1
                c = a >> comb()
        return out

    exp = sum(d << (i * 3) for i, d in enumerate(nums))

    possible = [0]

    for i in reversed(range(16)):
        new = []
        for j in range(8):
            for n in possible:
                inp = n + (j << i * 3)
                mask = (-1 << i * 3) & (8**16-1)
                if interpret(inp) & mask == exp & mask:
                    new += [inp]
        possible = new
        print(len(possible))
    print(min(possible))

fast_search()
