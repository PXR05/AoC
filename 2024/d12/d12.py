grid = open("input").read().splitlines()
w = len(grid[0])
h = len(grid)


def count_perimeter(i, j):
    count = 0
    char = grid[i][j]
    neighbors = []
    if i + 1 < h:
        if grid[i + 1][j] != char:
            count += 1
        else:
            neighbors.append((i + 1, j))
    else:
        count += 1
    if i - 1 >= 0:
        if grid[i - 1][j] != char:
            count += 1
        else:
            neighbors.append((i - 1, j))
    else:
        count += 1
    if j + 1 < w:
        if grid[i][j + 1] != char:
            count += 1
        else:
            neighbors.append((i, j + 1))
    else:
        count += 1
    if j - 1 >= 0:
        if grid[i][j - 1] != char:
            count += 1
        else:
            neighbors.append((i, j - 1))
    else:
        count += 1
    return (count, neighbors)


sections = []
for i, line in enumerate(grid):
    for j, char in enumerate(line):
        perimeter, neighbors = count_perimeter(i, j)
        is_new = True
        section_ref = None
        for section in sections:
            if char == section["char"] and any(
                n in section["chars"] for n in neighbors
            ):
                if section_ref is None:
                    section_ref = section
                    section_ref["chars"].add((i, j))
                    section_ref["perimeter"] += perimeter
                    section_ref["area"] += 1
                else:
                    # another match means the current char is a connection between two sections
                    section_ref["chars"].update(section["chars"])
                    section_ref["perimeter"] += section["perimeter"]
                    section_ref["area"] += section["area"]
                    sections.remove(section)
                is_new = False
        if is_new:
            sections.append(
                {"char": char, "area": 1, "perimeter": perimeter, "chars": {(i, j)}}
            )

print(sum(section["area"] * section["perimeter"] for section in sections))


def count_corners(section):
    corners = 0
    seen = set()
    corner_offsets = [(-0.5, -0.5), (0.5, -0.5), (0.5, 0.5), (-0.5, 0.5)]
    for i, j in section["chars"]:
        for offset_i, offset_j in corner_offsets:
            corner = (i + offset_i, j + offset_j)
            if corner in seen:
                continue
            seen.add(corner)
            # count chars next to corner
            adjacent = sum(
                (corner[0] + _i, corner[1] + _j) in section["chars"]
                for _i, _j in corner_offsets
            )
            if adjacent in (1, 3):
                corners += 1
            elif adjacent == 2:
                points = [
                    (corner[0] - 0.5, corner[1] - 0.5),
                    (corner[0] + 0.5, corner[1] + 0.5),
                ]
                # corner between diagonal chars
                if all(p in section["chars"] for p in points) or all(
                    p not in section["chars"] for p in points
                ):
                    corners += 2
    return corners


print(sum(section["area"] * count_corners(section) for section in sections))
