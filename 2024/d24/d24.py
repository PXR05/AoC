gates, operations = open("input").read().split("\n\n")
gates = {gate.split(": ")[0]: int(gate.split(": ")[1]) for gate in gates.split("\n")}
operations = [
    {
        "arg1": op.split(" -> ")[0].split(" ")[0],
        "arg2": op.split(" -> ")[0].split(" ")[2],
        "op": op.split(" -> ")[0].split(" ")[1],
        "out": op.split(" -> ")[1],
    }
    for op in operations.split("\n")
]


def eval(arg1, arg2, op):
    if op == "AND":
        return arg1 & arg2
    elif op == "OR":
        return arg1 | arg2
    elif op == "XOR":
        return arg1 ^ arg2
    return None


# P1
queue = operations.copy()
while queue:
    opr = queue.pop()
    arg1, arg2, op, out = opr.values()
    if gates.get(arg1) is None or gates.get(arg2) is None:
        queue.insert(0, opr)
        continue
    gates[out] = eval(gates[arg1], gates[arg2], op)

z_gates = sorted(
    [gate for gate in gates.items() if gate[0].startswith("z")],
    key=lambda x: x[0],
    reverse=True,
)
z_bin = "".join([str(gate[1]) for gate in z_gates])
print(int(z_bin, 2))


# P2
# Manual
x_bits = [gate[1] for gate in gates.items() if gate[0].startswith("x")]
y_bits = [gate[1] for gate in gates.items() if gate[0].startswith("y")]
expected_sum = int("".join([str(x) for x in x_bits]), 2) + int(
    "".join([str(y) for y in y_bits]), 2
)
expected_bin = bin(expected_sum)[2:].zfill(len(z_gates))
expected_bits = [int(bit) for bit in expected_bin]

mismatches = []
for i, (gate_name, gate_value) in enumerate(z_gates):
    if gate_value != expected_bits[i]:
        mismatches.append((gate_name, expected_bits[i]))

print(mismatches, "\nP2 was done manually")
