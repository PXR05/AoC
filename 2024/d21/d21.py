from functools import cache

codes = open("input").read().splitlines()

numpad = ["789", "456", "123", "X0A"]
dirpad = ["X^A", "<v>"]


def find(c, pad):
    for i, row in enumerate(pad):
        for j, char in enumerate(row):
            if char == c:
                return j, i
    assert False


def arrows(c1, c2, pad):
    x1, y1 = find(c1, pad)
    x2, y2 = find(c2, pad)
    xg, yg = find("X", pad)
    diff_x, diff_y = x2 - x1, y2 - y1

    v_moves = "v" * abs(diff_x) if diff_x >= 0 else "^" * abs(diff_x)
    h_moves = ">" * abs(diff_y) if diff_y >= 0 else "<" * abs(diff_y)

    if diff_x == diff_y == 0:
        return [""]
    elif diff_x == 0:
        return [h_moves]
    elif diff_y == 0:
        return [v_moves]
    elif (y1, x2) == (yg, xg):
        return [v_moves + h_moves]
    elif (y2, x1) == (yg, xg):
        return [h_moves + v_moves]
    else:
        return [v_moves + h_moves, h_moves + v_moves]


def cmds(seq, pad):
    res = []
    for c1, c2 in zip("A" + seq, seq):
        res += [[arrow + "A" for arrow in arrows(c1, c2, pad)]]
    return res


@cache
def solve(seq, depth):
    if depth == 1:
        return len(seq)
    if any(c in seq for c in "012345679"):
        pad = numpad
    else:
        pad = dirpad
    res = 0
    for cmd in cmds(seq, pad):
        res += min(solve(arrow, depth - 1) for arrow in cmd)
    return res


sum1 = 0
for code in codes:
    sum1 += solve(code, 1 + 2 + 1) * int(code[:3])
print(sum1)

sum2 = 0
for code in codes:
    sum2 += solve(code, 1 + 25 + 1) * int(code[:3])
print(sum2)
