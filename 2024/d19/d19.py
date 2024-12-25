towels, patterns = open("input").read().split("\n\n")
towels = set(towels.split(", "))
patterns = patterns.splitlines()

# P1
count = 0
for pattern in patterns:
    n = len(pattern)
    char_match = [False] * (n + 1)
    char_match[0] = True
    for i in range(n + 1):
        if not char_match[i]:
            continue
        for towel in towels:
            j = i + len(towel)
            if j <= n and pattern[i:j] == towel:
                char_match[j] = True
    if char_match[n]:
        count += 1
print(count)

# P2
count = 0
for pattern in patterns:
    n = len(pattern)
    ways = [0] * (n + 1)
    ways[0] = 1
    for i in range(n + 1):
        if ways[i] == 0:
            continue
        for towel in towels:
            j = i + len(towel)
            if j <= n and pattern[i:j] == towel:
                ways[j] += ways[i]
    count += ways[n]
print(count)
