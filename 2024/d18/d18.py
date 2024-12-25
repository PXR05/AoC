bytes = [
    (int(c[0]), int(c[1]))
    for c in [line.split(",") for line in open("input").read().strip().splitlines()]
]

# Change these values to 70, 70 and 1025 when using the full input
w, h = 6, 6
offset = 12


def path_length(grid, start, end):
    height = len(grid)
    width = len(grid[0])

    visited = [[False for _ in range(width)] for _ in range(height)]
    distances = [[0 for _ in range(width)] for _ in range(height)]

    to_visit = [(start[0], start[1])]
    visited[start[1]][start[0]] = True

    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while to_visit:
        curr_x, curr_y = to_visit.pop(0)
        if (curr_x, curr_y) == end:
            return distances[curr_y][curr_x]
        for dx, dy in moves:
            new_x = curr_x + dx
            new_y = curr_y + dy
            if (
                0 <= new_x < width
                and 0 <= new_y < height
                and not visited[new_y][new_x]
                and grid[new_y][new_x] == 0
            ):
                visited[new_y][new_x] = True
                distances[new_y][new_x] = distances[curr_y][curr_x] + 1
                to_visit.append((new_x, new_y))
    return -1


def sim_grid(to_drop):
    grid = []
    for y in range(w + 1):
        line = []
        for x in range(h + 1):
            if (x, y) in to_drop:
                line.append(1)
            else:
                line.append(0)
        grid.append(line)
    return grid


# P1
grid = sim_grid(bytes[:offset])
print(path_length(grid, (0, 0), (w, h)))


# P2
i = offset
dir = 1
step = (len(bytes) - offset) // 2
while True:
    grid = sim_grid(bytes[:i])
    next_grid = sim_grid(bytes[: i + 1])
    curr = path_length(grid, (0, 0), (w, h))
    next = path_length(next_grid, (0, 0), (w, h))
    if curr > -1 and next == -1:
        print(bytes[i])
        break
    if next == -1:
        i -= step
        if dir == 1:
            dir = -1
            step //= 2
    else:
        i += step
        if dir == -1:
            dir = 1
            step //= 2
