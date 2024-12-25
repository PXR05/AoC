grid = open("input").read().splitlines()

start_loc = []

for i, line in enumerate(grid):
    for j, char in enumerate(line):
        if char == "^":
            start_loc = [i, j]
            break
    if len(start_loc) > 0:
        break

# P1
visited = set()


def move_up(loc, curr_grid=grid, curr_visited=visited):
    y, x = loc
    for i in range(y, -1, -1):
        if curr_grid[i][x] == "#":
            new_loc = [i + 1, x]
            curr_visited.add(tuple(new_loc))
            return ["right", new_loc]
        curr_visited.add((i, x))
    return ["stop"]


def move_right(loc, curr_grid=grid, curr_visited=visited):
    y, x = loc
    for j in range(x + 1, len(curr_grid[0])):
        if curr_grid[y][j] == "#":
            new_loc = [y, j - 1]
            curr_visited.add(tuple(new_loc))
            return ["down", new_loc]
        curr_visited.add((y, j))
    return ["stop"]


def move_down(loc, curr_grid=grid, curr_visited=visited):
    y, x = loc
    for i in range(y + 1, len(curr_grid)):
        if curr_grid[i][x] == "#":
            new_loc = [i - 1, x]
            curr_visited.add(tuple(new_loc))
            return ["left", new_loc]
        curr_visited.add((i, x))
    return ["stop"]


def move_left(loc, curr_grid=grid, curr_visited=visited):
    y, x = loc
    for j in range(x - 1, -1, -1):
        if curr_grid[y][j] == "#":
            new_loc = [y, j + 1]
            curr_visited.add(tuple(new_loc))
            return ["up", new_loc]
        curr_visited.add((y, j))
    return ["stop"]


visited.add(tuple(start_loc))
new_loc = move_up(start_loc)
while new_loc[0] != "stop":
    match new_loc[0]:
        case "left":
            new_loc = move_left(new_loc[1])
        case "right":
            new_loc = move_right(new_loc[1])
        case "up":
            new_loc = move_up(new_loc[1])
        case "down":
            new_loc = move_down(new_loc[1])
print(len(visited))


# P2
def check_loop(obs_pos):
    test_grid = [list(row) for row in grid]
    test_grid[obs_pos[0]][obs_pos[1]] = "#"
    test_visited = set()

    test_visited.add(tuple(start_loc))
    new_loc = move_up(start_loc, test_grid, test_visited)
    seen_states = set()

    while new_loc[0] != "stop":
        state = (tuple(new_loc[1]), new_loc[0])
        if state in seen_states:
            return True
        seen_states.add(state)

        match new_loc[0]:
            case "left":
                new_loc = move_left(new_loc[1], test_grid, test_visited)
            case "right":
                new_loc = move_right(new_loc[1], test_grid, test_visited)
            case "up":
                new_loc = move_up(new_loc[1], test_grid, test_visited)
            case "down":
                new_loc = move_down(new_loc[1], test_grid, test_visited)
    return False


loop_count = sum(1 for pos in visited if pos != tuple(start_loc) and check_loop(pos))
print(loop_count)
