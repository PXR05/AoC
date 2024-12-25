input = open("input").read().strip().splitlines()
robots = []
for line in input:
    p, v = line.split(" ")
    p = tuple([int(n) for n in p.split("=")[-1].split(",")])
    v = tuple([int(n) for n in v.split("=")[-1].split(",")])
    robots.append((p, v))


# Change these values to 101, 103 and 1000000 (depends on input) when using the full input
w = 11
h = 7
n = 100


def move(robot):
    p, v = robot
    px, py = p
    vx, vy = v
    new_px = (px + vx) % w
    new_py = (py + vy) % h
    return ((new_px, new_py), v)


def check_consecutive_robots(robots, n=8):
    positions = set(p for p, _ in robots)
    for p, _ in robots:
        x, y = p
        if all((x + i, y) in positions for i in range(n)):
            return True
    return False


for i in range(n):
    for j in range(len(robots)):
        robots[j] = move(robots[j])
    if check_consecutive_robots(robots):
        print(i)
        break

quadrants = [0] * 4
for robot in robots:
    p, _ = robot
    x, y = p
    mid_x = w // 2
    mid_y = h // 2
    if x < mid_x and y < mid_y:  # top left
        quadrants[0] += 1
    elif x > mid_x and y < mid_y:  # top right
        quadrants[1] += 1
    elif x > mid_x and y > mid_y:  # bottom right
        quadrants[2] += 1
    elif x < mid_x and y > mid_y:  # bottom left
        quadrants[3] += 1

factor = 1
for q in quadrants:
    factor *= q
print(factor)
