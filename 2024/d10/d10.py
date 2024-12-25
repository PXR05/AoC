input = open("input").read().split("\n")
grid = []
for line in input:
    grid.append([int(n) for n in line])
w = len(grid[0])
h = len(grid)

trailheads = []
for i, line in enumerate(grid):
    for j, num in enumerate(line):
        if num == 0:
            trailheads.append([i, j])


def check_surround(i, j, n):
    dirs = []
    if j - 1 >= 0:
        if grid[i][j - 1] == n + 1:
            dirs.append([i, j - 1])
    if j + 1 < w:
        if grid[i][j + 1] == n + 1:
            dirs.append([i, j + 1])
    if i - 1 >= 0:
        if grid[i - 1][j] == n + 1:
            dirs.append([i - 1, j])
    if i + 1 < h:
        if grid[i + 1][j] == n + 1:
            dirs.append([i + 1, j])
    return dirs


def find_paths(head_i, head_j):
    paths = set()

    def path_to_string(visited):
        return ",".join(f"{x},{y}" for x, y in visited)

    def dfs(i, j, visited):
        if grid[i][j] == 9:
            paths.add(path_to_string(visited))
            return
        next_pos = check_surround(i, j, grid[i][j])
        for next_i, next_j in next_pos:
            if (next_i, next_j) not in visited:
                visited.add((next_i, next_j))
                dfs(next_i, next_j, visited)
                visited.remove((next_i, next_j))

    visited = {(head_i, head_j)}
    dfs(head_i, head_j, visited)
    return len(paths)


total = 0
for i, j in trailheads:
    score = find_paths(i, j)
    total += score

print(total)
