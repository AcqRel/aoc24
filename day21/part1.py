from functools import cache
import heapq

@cache
def shortest_seq(ch1, ch2, pads):
    assert isinstance(pads, tuple)

    if not pads:
        return ch2

    curr_pad, next_pads = pads[0], pads[1:]

    for y, row in enumerate(curr_pad):
        for x, c in enumerate(row):
            if c == ch1: px, py = x, y
            if c == ch2: tx, ty = x, y
    
    costs = { }
    states = []
    heapq.heappush(states, (0, "", px, py, "A"))
    out_seq = None
    while states:
        _, s, x, y, p_ch = heapq.heappop(states)
        if (x, y, p_ch) not in costs:
            costs[(x, y, p_ch)] = len(c)
        else:
            assert costs[(x, y, p_ch)] <= len(c)
            continue

        if (x, y) == (tx, ty):
            found_seq = s + shortest_seq(p_ch, "A", next_pads)
            if out_seq is None or len(found_seq) < len(out_seq):
                out_seq = found_seq

        for (x2, y2, ch) in [(x - 1, y, "<"), (x + 1, y, ">"), (x, y - 1, "^"), (x, y + 1, "v")]:
            try:
                assert curr_pad[y2][x2] != "x"
            except:
                continue
            new_seq = s + shortest_seq(p_ch, ch, next_pads)
            heapq.heappush(states, (len(new_seq), new_seq, x2, y2, ch))

    print(ch1, ch2, out_seq)

    return out_seq

def final_seq(seq, pads):
    prev_ch = "A"
    result = ""
    for c in seq:
        result += shortest_seq(prev_ch, c, pads)
        prev_ch = c
    return result

dirpad = ("x^A", "<v>")
keypad = ("789", "456", "123", "x0A")

total = 0
for seq in open(0):
    seq = seq.strip()
    total += int(seq[:-1]) * len(final_seq(seq, (keypad, dirpad, dirpad)))
print(total)
