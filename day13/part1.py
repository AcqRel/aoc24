lines = open(0).read()

tokens = 0
for group in lines.split("\n\n"):
    lines = group.strip().split("\n")

    x1 = int(lines[0].split(" ")[2][2:-1])
    y1 = int(lines[0].split(" ")[3][2:])
    x2 = int(lines[1].split(" ")[2][2:-1])
    y2 = int(lines[1].split(" ")[3][2:])
    xt = int(lines[2].split(" ")[1][2:-1])
    yt = int(lines[2].split(" ")[2][2:])

    det = x1 * y2 - x2 * y1
    assert det

    num_a = y2 * xt - x2 * yt
    num_b = -y1 * xt + x1 * yt

    print(num_a, num_b, det)
    if num_a % det == 0 and num_b % det == 0 and num_a/det >= 0 and num_b/det >= 0:
        print(num_a / det, num_b / det)

        tokens += num_a // det * 3 + num_b // det 

print(tokens)