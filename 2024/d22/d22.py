input = [int(line) for line in open("input").read().splitlines()]


def mix_prune(val, secret):
    temp = secret
    temp ^= val
    temp %= 16777216
    return temp


def evolve(secret):
    mul = secret * 64
    secret = mix_prune(mul, secret)
    div = secret // 32
    secret = mix_prune(div, secret)
    mul = secret * 2048
    secret = mix_prune(mul, secret)
    return secret


n = 2000
res = [input]
for j in range(n):
    temp = []
    for secret in res[-1]:
        temp.append(evolve(secret))
    res.append(temp)

# P1
print(sum(res[-1]))

# P2
memo = {}
for i in range(len(res[0])):
    seq = []
    for j in range(n + 1):
        seq.append(res[j][i] % 10)

    diffs = []
    for j in range(len(seq) - 1):
        diffs.append(seq[j + 1] - seq[j])

    seen = set()
    for p in range(4, len(diffs)):
        pattern = tuple(diffs[p - 3 : p + 1])
        if pattern not in memo and pattern not in seen:
            memo[pattern] = seq[p + 1]
        elif pattern not in seen:
            memo[pattern] += seq[p + 1]
        seen.add(pattern)

print(max(memo.values()))
