patterns = [p.splitlines() for p in open("input").read().strip().split("\n\n")]

h = len(patterns[0])
w = len(patterns[0][0])

keys = []
locks = []
for pattern in patterns:
    if pattern[0][0] == ".":
        heights = [None] * w
        for i, row in enumerate(pattern):
            for j, char in enumerate(row):
                if char == ".":
                    heights[j] = len(pattern) - i - 2
        keys.append(heights)
    else:
        heights = [None] * w
        for i, row in enumerate(pattern):
            for j, char in enumerate(row):
                if char == "#":
                    heights[j] = i
        locks.append(heights)

count = 0
for key in keys:
    for lock in locks:
        fit = True
        # print(key, lock, h - 2)
        for i in range(w):
            # print(key[i], lock[i], key[i] + lock[i])
            if key[i] + lock[i] > h - 2:
                fit = False
                break
        if fit:
            count += 1

print(count)
