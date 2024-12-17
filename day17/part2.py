import z3

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

with_z3()
