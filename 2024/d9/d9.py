input = [int(i) for i in open("input").read().strip("\n")]

# P1
files = []
for i, num in enumerate(input):
    for j in range(num):
        if i % 2 == 0:
            files.append(i - i // 2)
        else:
            files.append(".")

p_start = 0
p_end = len(files) - 1
while p_start != p_end:
    if files[p_start] == ".":
        while files[p_end] == ".":
            p_end -= 1
        files[p_start], files[p_end] = files[p_end], files[p_start]
    p_start += 1

checksum = 0
for i, f in enumerate(files):
    if f == ".":
        break
    checksum += i * f

print(checksum)

# P2
file_map = {}
empty_map = {}
for i, num in enumerate(input):
    if i % 2 == 0:
        file_map[i - i // 2] = num
    else:
        empty_map[i - i // 2 - 1] = num

files = ["."] * sum(input)
pos = 0
for i in range(len(file_map)):
    file_len = file_map[i]
    for _ in range(file_len):
        files[pos] = i
        pos += 1
    if i in empty_map:
        pos += empty_map[i]

for id in sorted(file_map.keys(), reverse=True):
    file_len = file_map[id]
    p_start = files.index(id)
    p_curr = 0
    while p_curr < p_start:
        space = 0
        for i in range(p_curr, len(files)):
            if files[i] == ".":
                space += 1
            else:
                break
        if space >= file_len:
            files[p_curr : p_curr + file_len] = [id] * file_len
            files[p_start : p_start + file_len] = ["."] * file_len
            break
        p_curr = i + 1

checksum = 0
for i, f in enumerate(files):
    if f != ".":
        checksum += i * f

print(checksum)
