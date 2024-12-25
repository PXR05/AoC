grid = [list(line) for line in open("input").read().splitlines()]


def find_start_end():
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "S":
                start = (x, y)
            elif grid[y][x] == "E":
                end = (x, y)
                return start, end


def get_distances(source):
    distances = {source: 0}
    queue = [(source, 0)]
    i = 0
    while i < len(queue):
        pos, dist = queue[i]
        i += 1
        x, y = pos
        moves = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        for dx, dy in moves:
            if (
                (dx, dy) not in distances
                and 0 <= dy < len(grid)
                and 0 <= dx < len(grid[0])
                and grid[dy][dx] != "#"
            ):
                distances[(dx, dy)] = dist + 1
                queue.append(((dx, dy), dist + 1))
    return distances


def find_cheats(min_savings, cheat_range):
    cheats = 0
    start, end = find_start_end()
    start_distances = get_distances(start)
    end_distances = get_distances(end)
    base_time = start_distances.get(end, float("inf"))
    reachable = set(start_distances.keys())

    for pos1 in reachable:
        x1, y1 = pos1
        time_to_cheat = start_distances[pos1]

        for dx in range(-cheat_range, cheat_range + 1):
            for dy in range(-cheat_range, cheat_range + 1):
                if abs(dx) + abs(dy) > cheat_range:
                    continue
                x2, y2 = x1 + dx, y1 + dy
                pos2 = (x2, y2)
                if (
                    pos2 in end_distances
                    and 0 <= y2 < len(grid)
                    and 0 <= x2 < len(grid[0])
                ):
                    total_time = time_to_cheat + abs(dx) + abs(dy) + end_distances[pos2]
                    if base_time - total_time >= min_savings:
                        cheats += 1
    return cheats


print(find_cheats(100, 2))
print(find_cheats(100, 20))
