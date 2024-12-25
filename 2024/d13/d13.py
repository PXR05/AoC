input = [machine.split("\n") for machine in open("input").read().strip().split("\n\n")]

machines = []
for machine in input:
    m = {}
    button_a = machine[0].split(": ")[-1].split(", ")
    m["a"] = [int(button_a[0].split("+")[-1]), int(button_a[1].split("+")[-1])]
    button_b = machine[1].split(": ")[-1].split(", ")
    m["b"] = [int(button_b[0].split("+")[-1]), int(button_b[1].split("+")[-1])]
    prize = machine[2].split(": ")[-1].split(", ")
    m["prize"] = [int(prize[0].split("=")[-1]), int(prize[1].split("=")[-1])]
    machines.append(m)


# P1
def get_tokens_bruteforce(machine):
    max_tries = 100
    a_moves = machine["a"]
    b_moves = machine["b"]
    prize = machine["prize"]
    for a_presses in range(max_tries + 1):
        for b_presses in range(max_tries + 1):
            x = a_presses * a_moves[0] + b_presses * b_moves[0]
            y = a_presses * a_moves[1] + b_presses * b_moves[1]
            if x == prize[0] and y == prize[1]:
                return a_presses * 3 + b_presses
    return None


p1_tokens = 0
for machine in machines:
    tokens = get_tokens_bruteforce(machine)
    if tokens is not None:
        p1_tokens += tokens

print(p1_tokens)


# P2
def get_tokens_formula(machine, offset=10000000000000):
    x1, y1 = machine["a"]
    x2, y2 = machine["b"]
    xp, yp = machine["prize"]
    xp += offset
    yp += offset
    # xp = a.x1 + b.x2
    # yp = a.y1 + b.y2

    # a = (xp - b.x2) / x1

    # yp = y1.((xp - b.x2) / x1) + b.y2
    # yp - b.y2 = (xp.y1 - b.x2.y1) / x1
    # x1.yp - b.x1.y2 = xp.y1 - b.x2.y1
    # b.x2.y1 - b.x1.y2 = xp.y1 - x1.yp
    # b.(x2.y1 - x1.y2) = xp.y1 - x1.yp
    # b = (xp.y1 - x1.yp) / (x2.y1 - x1.y2)
    b = (xp * y1 - x1 * yp) / (x2 * y1 - x1 * y2)
    a = (xp - b * x2) / x1
    if a.is_integer() and b.is_integer():
        return int(a) * 3 + int(b)
    return None


p2_tokens = 0
for machine in machines:
    tokens = get_tokens_formula(machine)
    if tokens is not None:
        p2_tokens += tokens

print(p2_tokens)
