from heapq import heappush, heappop

grid = [list(line) for line in open("input").read().strip().splitlines()]


def find_start_end():
    start = end = None
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "S":
                start = (x, y)
            elif grid[y][x] == "E":
                end = (x, y)
    return start, end


def get_paths():
    start, end = find_start_end()
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    heap = []
    heappush(heap, (0, start[0], start[1], 0, {(start[0], start[1])}))
    visited = {(start[0], start[1], 0): 0}
    best_score = float("inf")
    best_paths = set()

    while heap:
        score, x, y, dir, path = heappop(heap)

        if score > best_score:
            continue

        if (x, y) == end:
            if score < best_score:
                best_score = score
                best_paths = path
            elif score == best_score:
                best_paths.update(path)
            continue

        for turn in [-1, 1]:
            new_dir = (dir + turn) % 4
            new_score = score + 1000
            state = (x, y, new_dir)
            if state not in visited or new_score <= visited[state]:
                visited[state] = new_score
                heappush(heap, (new_score, x, y, new_dir, path.copy()))

        dx, dy = directions[dir]
        new_x, new_y = x + dx, y + dy
        if (
            0 <= new_x < len(grid[0])
            and 0 <= new_y < len(grid)
            and grid[new_y][new_x] != "#"
        ):
            new_score = score + 1
            new_path = path.copy()
            new_path.add((new_x, new_y))
            state = (new_x, new_y, dir)
            if state not in visited or new_score <= visited[state]:
                visited[state] = new_score
                heappush(heap, (new_score, new_x, new_y, dir, new_path))

    return best_score, len(best_paths)


score, count = get_paths()
print(score)
print(count)
