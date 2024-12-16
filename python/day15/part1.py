first_part = True

m = []
instrs = []

while True:
    try:
        line = input()
        if len(line) == 0:
            first_part = False
        elif first_part:
            m.append(list(line))
        else:
            instrs.extend(list(line))
    except EOFError:
        break

for inst in instrs:
    robot_pos = None
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == "@":
                robot_pos = (i, j)
    robot_row, robot_col = robot_pos

    if inst == "^":
        if m[robot_row - 1][robot_col] == ".":
            m[robot_row - 1][robot_col] = "@"
            m[robot_row][robot_col] = "."
            continue

        next_wall_row_idx = 0
        for row in range(robot_row):
            if m[row][robot_col] == "#":
                next_wall_row_idx = row

        open_cell_row_idx = None
        for i in range(next_wall_row_idx + 1, robot_row):
            if m[i][robot_col] == ".":
                open_cell_row_idx = i

        if open_cell_row_idx is None:
            continue

        for i in range(open_cell_row_idx, robot_row):
            m[i][robot_col] = m[i + 1][robot_col]

        m[robot_row][robot_col] = "."
    elif inst == ">":
        if m[robot_row][robot_col + 1] == ".":
            m[robot_row][robot_col + 1] = "@"
            m[robot_row][robot_col] = "."
            continue

        next_wall_col_idx = 0
        for col in reversed(range(robot_col + 1, len(m[0]))):
            if m[robot_row][col] == "#":
                next_wall_col_idx = col

        open_cell_col_idx = None
        for j in reversed(range(robot_col + 1, next_wall_col_idx)):
            if m[robot_row][j] == ".":
                open_cell_col_idx = j

        if open_cell_col_idx is None:
            continue

        for j in reversed(range(robot_col + 1, open_cell_col_idx + 1)):
            m[robot_row][j] = m[robot_row][j - 1]

        m[robot_row][robot_col] = "."
    elif inst == "v":
        if m[robot_row + 1][robot_col] == ".":
            m[robot_row + 1][robot_col] = "@"
            m[robot_row][robot_col] = "."
            continue

        next_wall_row_idx = 0
        for row in reversed(range(robot_row + 1, len(m))):
            if m[row][robot_col] == "#":
                next_wall_row_idx = row

        open_cell_row_idx = None
        for i in reversed(range(robot_row + 1, next_wall_row_idx)):
            if m[i][robot_col] == ".":
                open_cell_row_idx = i

        if open_cell_row_idx is None:
            continue

        for i in reversed(range(robot_row + 1, open_cell_row_idx + 1)):
            m[i][robot_col] = m[i - 1][robot_col]

        m[robot_row][robot_col] = "."
    elif inst == "<":
        if m[robot_row][robot_col - 1] == ".":
            m[robot_row][robot_col - 1] = "@"
            m[robot_row][robot_col] = "."
            continue

        next_wall_col_idx = 0
        for col in range(robot_col):
            if m[robot_row][col] == "#":
                next_wall_col_idx = col

        open_cell_col_idx = None
        for j in range(next_wall_col_idx + 1, robot_col):
            if m[robot_row][j] == ".":
                open_cell_col_idx = j

        if open_cell_col_idx is None:
            continue

        for j in range(open_cell_col_idx, robot_col):
            m[robot_row][j] = m[robot_row][j + 1]

        m[robot_row][robot_col] = "."
    else:
        raise Exception("invalid instruction")


gps_sum = 0
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] == "O":
            gps_sum += 100 * i + j

print(gps_sum)
