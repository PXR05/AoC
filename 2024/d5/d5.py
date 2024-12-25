rules = []
prints = []
restricted_numbers = []
with open("input", "r") as f:
    for line in f:
        if "|" in line:
            split = line.strip("\n").split("|")
            restricted_numbers.extend(split)
            rules.append(split)
        elif "," in line:
            prints.append(line.strip("\n").split(","))
restricted_numbers = set(restricted_numbers)


def is_valid(seq):
    for r in rules:
        try:
            before = seq.index(r[0])
            after = seq.index(r[1])
            if before > after:
                return False
        except ValueError:
            continue
    return True


def topological_sort(seq):
    graph = {x: set() for x in seq}
    for r in rules:
        if r[0] in seq and r[1] in seq:
            graph[r[0]].add(r[1])

    result = []
    visited = set()
    temp_visited = set()

    def visit(n):
        if n in temp_visited:
            return False
        if n in visited:
            return True
        temp_visited.add(n)

        for m in graph[n]:
            if not visit(m):
                return False

        temp_visited.remove(n)
        visited.add(n)
        result.insert(0, n)
        return True

    for n in seq:
        if n not in visited:
            if not visit(n):
                return None
    return result


corrects = []
incorrects = []
for p in prints:
    if is_valid(p):
        corrects.append(p)
    else:
        incorrects.append(p)

correct_middles = [int(c[int(len(c) / 2)]) for c in corrects]
correct_sum = sum(correct_middles)

# P1
print(correct_sum)

corrected = []
for seq in incorrects:
    res = topological_sort(seq)
    if res:
        corrected.append(res)

corrected_middles = [int(c[int(len(c) / 2)]) for c in corrected]
corrected_sum = sum(corrected_middles)

# P2
print(corrected_sum)
