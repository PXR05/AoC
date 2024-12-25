map_data, moves = open("input").read().split("\n\n")
grid = [list(row) for row in map_data.split("\n")]
moves = [move for move in moves if move in "<>^v"]


# P1
rows = len(grid)
cols = len(grid[0])
walls = set()
boxes = set()
robot = None

for i, row in enumerate(grid):
    for j, c in enumerate(row):
        if c == "#":
            walls.add((i, j))
        elif c == "O":
            boxes.add((i, j))
        elif c == "@":
            robot = (i, j)


def move_boxes(direction):
    global robot
    i, j = robot
    chain = [robot]

    if direction == ">":
        j += 1
        while (i, j) in boxes:
            chain.insert(0, (i, j))
            j += 1
        if (i, j) not in walls:
            for b in chain[:-1]:
                boxes.remove(b)
                boxes.add((b[0], b[1] + 1))
            robot = (robot[0], robot[1] + 1)
    elif direction == "<":
        j -= 1
        while (i, j) in boxes:
            chain.insert(0, (i, j))
            j -= 1
        if (i, j) not in walls:
            for b in chain[:-1]:
                boxes.remove(b)
                boxes.add((b[0], b[1] - 1))
            robot = (robot[0], robot[1] - 1)
    elif direction == "^":
        i -= 1
        while (i, j) in boxes:
            chain.insert(0, (i, j))
            i -= 1
        if (i, j) not in walls:
            for b in chain[:-1]:
                boxes.remove(b)
                boxes.add((b[0] - 1, b[1]))
            robot = (robot[0] - 1, robot[1])
    elif direction == "v":
        i += 1
        while (i, j) in boxes:
            chain.insert(0, (i, j))
            i += 1
        if (i, j) not in walls:
            for b in chain[:-1]:
                boxes.remove(b)
                boxes.add((b[0] + 1, b[1]))
            robot = (robot[0] + 1, robot[1])


for move in moves:
    move_boxes(move)
total = sum(100 * b[0] + b[1] for b in boxes)
print(total)


# P2
rows = len(grid)
cols = len(grid[0]) * 2
walls = set()
left_boxes = set()
right_boxes = set()
robot = None

for i, row in enumerate(grid):
    for j, c in enumerate(row):
        if c == "#":
            walls.add((i, 2 * j))
            walls.add((i, 2 * j + 1))
        elif c == "O":
            left_boxes.add((i, 2 * j))
            right_boxes.add((i, 2 * j + 1))
        elif c == "@":
            robot = (i, 2 * j)


def move_vertical(direction, robot, left_boxes, right_boxes):
    chain = {robot}
    boxes_to_process = set()
    i, j = robot
    di = 1 if direction == "v" else -1
    i += di

    if (i, j) in walls:
        return robot, left_boxes, right_boxes

    if (i, j) in left_boxes:
        boxes_to_process.add((i, j))
        boxes_to_process.add((i, j + 1))
    elif (i, j) in right_boxes:
        boxes_to_process.add((i, j - 1))
        boxes_to_process.add((i, j))

    wall_hit = False
    while boxes_to_process:
        b = boxes_to_process.pop()
        chain.add(b)
        i, j = b
        i += di
        if (i, j) in walls:
            wall_hit = True
            continue
        elif (i, j) in left_boxes:
            boxes_to_process.add((i, j))
            boxes_to_process.add((i, j + 1))
        elif (i, j) in right_boxes:
            boxes_to_process.add((i, j))
            boxes_to_process.add((i, j - 1))

    if wall_hit:
        return robot, left_boxes, right_boxes

    old_left = set()
    new_left = set()
    old_right = set()
    new_right = set()

    new_robot = robot
    for b in chain:
        if b == robot:
            new_robot = (robot[0] + di, robot[1])
        elif b in left_boxes:
            old_left.add(b)
            new_left.add((b[0] + di, b[1]))
        else:
            old_right.add(b)
            new_right.add((b[0] + di, b[1]))

    return (
        new_robot,
        (left_boxes - old_left) | new_left,
        (right_boxes - old_right) | new_right,
    )


def move_horizontal(direction, robot, left_boxes, right_boxes):
    chain = [robot]
    i, j = robot
    dj = 2 if direction == ">" else -2
    j += dj // 2

    new_robot = robot
    if direction == ">":
        while (i, j) in left_boxes:
            chain.insert(0, (i, j))
            chain.insert(0, (i, j + 1))
            j += 2
        if (i, j) not in walls:
            for b in chain[:-1:2]:
                right_boxes = right_boxes - {b} | {(b[0], b[1] + 1)}
                left_boxes = left_boxes - {(b[0], b[1] - 1)} | {(b[0], b[1])}
            new_robot = (robot[0], robot[1] + 1)
    else:  # left
        while (i, j) in right_boxes:
            chain.insert(0, (i, j))
            chain.insert(0, (i, j - 1))
            j -= 2
        if (i, j) not in walls:
            for b in chain[:-1:2]:
                left_boxes = left_boxes - {b} | {(b[0], b[1] - 1)}
                right_boxes = right_boxes - {(b[0], b[1] + 1)} | {b}
            new_robot = (robot[0], robot[1] - 1)

    return new_robot, left_boxes, right_boxes


for move in moves:
    if move in "^v":
        robot, left_boxes, right_boxes = move_vertical(
            move, robot, left_boxes, right_boxes
        )
    else:
        robot, left_boxes, right_boxes = move_horizontal(
            move, robot, left_boxes, right_boxes
        )
p2_total = sum(100 * b[0] + b[1] for b in left_boxes)
print(p2_total)
