input = [tuple(line.split("-")) for line in open("input").read().splitlines()]

conns = {}
for a, b in input:
    if conns.get(a) is None:
        conns[a] = set()
    conns[a].add(b)
    if conns.get(b) is None:
        conns[b] = set()
    conns[b].add(a)

# P1
triples = set()
for c1 in conns:
    for c2 in conns[c1]:
        for c3 in conns[c1]:
            if c2 >= c3:
                continue
            if c2 in conns[c3]:
                triple = tuple(sorted([c1, c2, c3]))
                triples.add(triple)

count = 0
for triple in triples:
    if any(c[0] == "t" for c in triple):
        count += 1
print(count)


# P2
def is_connected(conns, graph):
    for c1 in conns:
        for c2 in conns:
            if c1 != c2 and c2 not in graph[c1]:
                return False
    return True


largest_group = set()
for c1 in conns:
    for c2 in conns[c1]:
        group = {c1, c2}
        for c3 in conns:
            if c3 in group:
                continue
            test_group = group | {c3}
            if is_connected(test_group, conns):
                group.add(c3)
        if len(group) > len(largest_group):
            largest_group = group
print(",".join(sorted(largest_group)))
