grid = open("input").read().split("\n")
width = len(grid[0])
height = len(grid)

antennas = {}
for i, line in enumerate(grid):
    for j, char in enumerate(line):
        if char != ".":
            if antennas.get(char) is None:
                antennas[char] = []
            antennas[char].append([i, j])


def p1(antennas):
    antinodes = set()
    for _, locations in antennas.items():
        for i in range(len(locations)):
            for j in range(i + 1, len(locations)):
                src_x, src_y = locations[i]
                pair_x, pair_y = locations[j]
                x_diff = pair_x - src_x
                y_diff = pair_y - src_y
                a1_x = src_x - x_diff
                a1_y = src_y - y_diff
                a2_x = pair_x + x_diff
                a2_y = pair_y + y_diff
                if 0 <= a1_x < height and 0 <= a1_y < width:
                    antinodes.add((a1_x, a1_y))
                if 0 <= a2_x < height and 0 <= a2_y < width:
                    antinodes.add((a2_x, a2_y))
    return len(antinodes)


print(p1(antennas))


def p2(antennas):
    antinodes = set()
    for _, locations in antennas.items():
        for i in range(len(locations)):
            antinodes.add(tuple(locations[i]))
            for j in range(i + 1, len(locations)):
                src_x, src_y = locations[i]
                pair_x, pair_y = locations[j]
                x_diff = pair_x - src_x
                y_diff = pair_y - src_y
                src_count = 0
                while True:
                    src_count += 1
                    src_a_x = src_x - (x_diff * src_count)
                    src_a_y = src_y - (y_diff * src_count)
                    if 0 <= src_a_x < height and 0 <= src_a_y < width:
                        antinodes.add((src_a_x, src_a_y))
                    else:
                        break
                pair_count = 0
                while True:
                    pair_count += 1
                    pair_a_x = pair_x + (x_diff * pair_count)
                    pair_a_y = pair_y + (y_diff * pair_count)
                    if 0 <= pair_a_x < height and 0 <= pair_a_y < width:
                        antinodes.add((pair_a_x, pair_a_y))
                    else:
                        break
    return len(antinodes)


print(p2(antennas))
