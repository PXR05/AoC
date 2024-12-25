import re

input = open("input").read().replace("\n", "")

# P1
pattern = r"mul\([0-9]+,[0-9]+\)"
valid = re.findall(pattern, input)
sum = 0
for v in valid:
    split = v.split("(")[1].split(")")[0].split(",")
    sum += int(split[0]) * int(split[1])
print(sum)

# P2
disable_pattern = r"don't\(\)"
disable_split = re.split(disable_pattern, input)
to_check = [disable_split[0]]
for i, s in enumerate(disable_split[1:]):
    enable_pattern = r"do\(\)"
    enable_split = re.split(enable_pattern, s)[1:]
    to_check.extend(enable_split)
sum = 0
pattern = r"mul\([0-9]+,[0-9]+\)"
for s in to_check:
    valid = re.findall(pattern, s)
    for v in valid:
        split = v.split("(")[1].split(")")[0].split(",")
        sum += int(split[0]) * int(split[1])
print(sum)
