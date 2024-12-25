input = open("input").read().splitlines()

left = [x.split("   ")[0] for x in input]
right = [x.split("   ")[-1].replace("\n", "") for x in input]

# P1
l_sorted = sorted(left)
r_sorted = sorted(right)
sum = 0
for i in range(1000):
    sum += abs(int(l_sorted[i]) - int(r_sorted[i]))

print(sum)

# P2
cm = {}
for r in right:
    c = cm.get(r, 0)
    cm[r] = c + 1

score = 0
for l in left:
    c = cm.get(l, 0)
    score += int(l) * c

print(score)
