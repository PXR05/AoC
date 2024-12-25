regs, codes = open("input").read().split("\n\n")
regs = [int(reg.split(": ")[-1]) for reg in regs.splitlines()]
codes = [int(code) for code in codes.split(": ")[-1].split(",")]


def to_str(arr):
    return ",".join([str(num) for num in arr])


def combo(op):
    if op <= 3:
        return op
    if op <= 6:
        return regs[op - 4]
    return None


def exec(code, op):
    global i
    if code == 3:
        if regs[0] != 0:
            i = op - 2
        return
    match code:
        case 0:
            regs[0] = regs[0] // (2 ** combo(op))
        case 1:
            regs[1] = regs[1] ^ op
        case 2:
            regs[1] = combo(op) % 8
        case 4:
            regs[1] = regs[1] ^ regs[2]
        case 5:
            out.append(combo(op) % 8)
        case 6:
            regs[1] = regs[0] // (2 ** combo(op))
        case 7:
            regs[2] = regs[0] // (2 ** combo(op))


# P1
out = []
i = 0
while i < len(codes) - 1:
    exec(codes[i], codes[i + 1])
    i += 2
print(to_str(out))


# P2
def search_a(base=0, n=15):
    if n < 0:
        return base
    res = []
    for x in range(8):
        a = base + x * (8**n)
        regs[0] = a
        regs[1] = 0
        regs[2] = 0
        global i, out
        i = 0
        out = []
        while i < len(codes) - 1:
            exec(codes[i], codes[i + 1])
            i += 2
        if len(out) == len(codes) and out[n] == codes[n]:
            result = search_a(a, n - 1)
            res.append(result)
    return min(res) if res else float("inf")


print(search_a())
