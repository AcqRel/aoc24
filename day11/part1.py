old = list(map(int, input().split())) 

for _ in range(25):
    new = []
    for n in old:
        if n == 0:
            new += [1]
        elif len(str(n)) % 2 == 0:
            i = len(str(n)) // 2
            new += [int(str(n)[:i]), int(str(n)[i:])]
        else:
            new += [n * 2024]

    old = new
print(len(new))