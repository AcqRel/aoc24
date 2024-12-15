old = list(map(int, input().split())) 

cache = {}
def size_of(num, iters):
    if not iters:
        return 1
    key = (num, iters)
    if key not in cache:
        n = num
        if n == 0:
            cache[key] = size_of(1, iters - 1)
        elif len(str(n)) % 2 == 0:
            i = len(str(n)) // 2
            cache[key] = size_of(int(str(n)[:i]), iters - 1) + size_of(int(str(n)[i:]), iters - 1)
        else:
            cache[key] = size_of(n * 2024, iters - 1)

    return cache[key]

print(sum(size_of(n, 75) for n in old))