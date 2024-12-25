input = open("input").read().splitlines()

# P1
count = 0
for line in input:
    lvls = line.replace("\n", "").split(" ")
    safe = True
    sign = 0
    for i in range(len(lvls) - 1):
        diff = int(lvls[i]) - int(lvls[i + 1])
        if i == 0:
            sign = diff
        elif (diff < 0 and sign > 0) or (diff > 0 and sign < 0):
            safe = False
            break
        if abs(diff) < 1 or abs(diff) > 3:
            safe = False
            break
    if safe:
        count += 1
print(count)


# P2
def is_safe(levels):
    if len(levels) < 2:
        return True
    sign = 0
    for i in range(len(levels) - 1):
        diff = int(levels[i]) - int(levels[i + 1])
        if i == 0:
            sign = diff
        elif (diff < 0 and sign > 0) or (diff > 0 and sign < 0):
            return False
        if abs(diff) < 1 or abs(diff) > 3:
            return False
    return True


count = 0
for line in input:
    lvls = line.replace("\n", "").split(" ")
    if is_safe(lvls):
        count += 1
        continue
    for i in range(len(lvls)):
        test_lvls = lvls[:i] + lvls[i + 1 :]
        if is_safe(test_lvls):
            count += 1
            break

print(count)
