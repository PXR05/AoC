lines = open("input").read().splitlines()


# P1
def p1(lines):
    key = "XMAS"
    count = 0

    def search_horizontal(lines):
        nonlocal count
        for line in lines:
            for i in range(len(line) - len(key) + 1):
                if line[i : i + 4] == key:
                    count += 1
                if line[i : i + 4] == key[::-1]:
                    count += 1

    def search_vertical(lines):
        transposed = [
            [lines[j][i] for j in range(len(lines))] for i in range(len(lines[0]))
        ]
        for i in range(len(transposed)):
            transposed[i] = "".join(transposed[i])
        search_horizontal(transposed)

    def search_diagonal(lines):
        rows = len(lines)
        cols = len(lines[0])
        for k in range(-(rows - 1), cols):
            diag = ""
            for i in range(rows):
                j = k + i
                if 0 <= j < cols:
                    diag += lines[i][j]
            if len(diag) >= 4:
                search_horizontal([diag])

        for k in range(cols + rows - 1):
            diag = ""
            for i in range(rows):
                j = k - i
                if 0 <= j < cols:
                    diag += lines[i][j]
            if len(diag) >= 4:
                search_horizontal([diag])

    search_horizontal(lines)
    search_vertical(lines)
    search_diagonal(lines)

    print(count)


p1(lines)


def p2(lines):
    key = "MAS"
    count = 0
    rows = len(lines)
    cols = len(lines[0])

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if lines[i][j] != "A":
                continue
            corners = [
                (lines[i - 1][j - 1], lines[i + 1][j + 1]),  # LT, RB
                (lines[i - 1][j + 1], lines[i + 1][j - 1]),  # RT, LB
            ]
            valid = 0
            for l, r in corners:
                pattern = l + "A" + r
                if pattern in [key, key[::-1]]:
                    valid += 1
            if valid == 2:
                count += 1

    print(count)


p2(lines)
