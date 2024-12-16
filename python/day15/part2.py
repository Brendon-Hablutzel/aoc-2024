# NOTE: this assumes that all crates can be moved, so be sure to use `can_move()` first
def move_crate_vertical(expanded_m, left_pos, direction):
    left_row, left_col = left_pos
    right_row, right_col = left_row, left_col + 1
    if direction == "^":
        above_left_row, above_left_col = left_row - 1, left_col
        above_right_row, above_right_col = right_row - 1, right_col

        above_left = expanded_m[above_left_row][above_left_col]
        above_right = expanded_m[above_right_row][above_right_col]

        if above_left == "." and above_right == ".":
            pass  # nothing to do here
        elif above_left == "]" or above_right == "[":
            if above_left == "]":
                move_crate_vertical(
                    expanded_m, (above_left_row, above_left_col - 1), "^"
                )
            if above_right == "[":
                move_crate_vertical(expanded_m, (above_right_row, above_right_col), "^")
        elif above_left == "[" and above_right == "]":
            move_crate_vertical(expanded_m, (above_left_row, above_left_col), "^")
        else:
            raise Exception("invalid box config when moving up")

        expanded_m[above_left_row][above_left_col] = "["
        expanded_m[above_right_row][above_right_col] = "]"

        expanded_m[left_row][left_col] = "."
        expanded_m[right_row][right_col] = "."
    elif direction == "v":
        below_left_row, below_left_col = left_row + 1, left_col
        below_right_row, below_right_col = right_row + 1, right_col

        below_left = expanded_m[below_left_row][below_left_col]
        below_right = expanded_m[below_right_row][below_right_col]

        if below_left == "." and below_right == ".":
            pass  # nothing to do here
        elif below_left == "]" or below_right == "[":
            if below_left == "]":
                move_crate_vertical(
                    expanded_m, (below_left_row, below_left_col - 1), "v"
                )
            if below_right == "[":
                move_crate_vertical(expanded_m, (below_right_row, below_right_col), "v")
        elif below_left == "[" and below_right == "]":
            move_crate_vertical(expanded_m, (below_left_row, below_left_col), "v")
        else:
            raise Exception("invalid box config when moving down")

        expanded_m[below_left_row][below_left_col] = "["
        expanded_m[below_right_row][below_right_col] = "]"

        expanded_m[left_row][left_col] = "."
        expanded_m[right_row][right_col] = "."
    else:
        raise Exception("bad direction when moving")


def can_move_vertical(expanded_m, crate_left_pos, direction):
    crate_left_row, crate_left_col = crate_left_pos
    crate_right_row, crate_right_col = crate_left_row, crate_left_col + 1
    if direction == "^":
        above_left_row, above_left_col = crate_left_row - 1, crate_left_col
        above_right_row, above_right_col = crate_right_row - 1, crate_right_col

        above_left = expanded_m[above_left_row][above_left_col]
        above_right = expanded_m[above_right_row][above_right_col]

        if above_left == "#" or above_right == "#":
            return False
        elif above_left == "." and above_right == ".":
            return True
        elif above_left == "]" or above_right == "[":
            both_valid = True
            if above_left == "]":
                if not can_move_vertical(
                    expanded_m, (above_left_row, above_left_col - 1), "^"
                ):
                    both_valid = False
            if above_right == "[":
                if not can_move_vertical(
                    expanded_m, (above_right_row, above_right_col), "^"
                ):
                    both_valid = False
            return both_valid
        elif above_left == "[" and above_right == "]":
            return can_move_vertical(expanded_m, (above_left_row, above_left_col), "^")
        else:
            raise Exception("invalid box config above when checking")
    elif direction == "v":
        below_left_row, below_left_col = crate_left_row + 1, crate_left_col
        below_right_row, below_right_col = crate_right_row + 1, crate_right_col

        below_left = expanded_m[below_left_row][below_left_col]
        below_right = expanded_m[below_right_row][below_right_col]

        if below_left == "#" or below_right == "#":
            return False
        elif below_left == "." and below_right == ".":
            return True
        elif below_left == "]" or below_right == "[":
            both_valid = True
            if below_left == "]":
                if not can_move_vertical(
                    expanded_m, (below_left_row, below_left_col - 1), "v"
                ):
                    both_valid = False
            if below_right == "[":
                if not can_move_vertical(
                    expanded_m, (below_right_row, below_right_col), "v"
                ):
                    both_valid = False
            return both_valid
        elif below_left == "[" and below_right == "]":
            return can_move_vertical(expanded_m, (below_left_row, below_left_col), "v")
        else:
            raise Exception(
                "invalid box config down when checking "
                + below_left
                + " "
                + below_right
            )
    else:
        raise Exception("bad direction when checking")


def can_move_right(expanded_m, crate_left_pos):
    left_row, left_col = crate_left_pos

    right_adj_row, right_adj_col = left_row, left_col + 2
    right_adj_cell = expanded_m[right_adj_row][right_adj_col]

    if right_adj_cell == "#":
        return False
    elif right_adj_cell == ".":
        return True
    elif right_adj_cell == "[":
        return can_move_right(expanded_m, (right_adj_row, right_adj_col))
    else:
        raise Exception("invalid position checking right " + right_adj_cell)


def move_right(expanded_m, crate_left_pos):
    left_row, left_col = crate_left_pos

    right_adj_row, right_adj_col = left_row, left_col + 2
    right_adj_cell = expanded_m[right_adj_row][right_adj_col]

    if right_adj_cell == ".":
        expanded_m[right_adj_row][right_adj_col] = "]"
        expanded_m[right_adj_row][right_adj_col - 1] = "["

        expanded_m[left_row][left_col] = "."
    elif right_adj_cell == "[":
        move_right(expanded_m, (right_adj_row, right_adj_col))
        expanded_m[right_adj_row][right_adj_col] = "]"
        expanded_m[right_adj_row][right_adj_col - 1] = "["

        expanded_m[left_row][left_col] = "."
    else:
        raise Exception("invalid position moving right " + right_adj_cell)


def can_move_left(expanded_m, crate_left_pos):
    left_row, left_col = crate_left_pos

    left_adj_row, left_adj_col = left_row, left_col - 1
    left_adj_cell = expanded_m[left_adj_row][left_adj_col]

    if left_adj_cell == "#":
        return False
    elif left_adj_cell == ".":
        return True
    elif left_adj_cell == "]":
        return can_move_left(expanded_m, (left_adj_row, left_adj_col - 1))
    else:
        raise Exception("invalid position checking left")


def move_left(expanded_m, crate_left_pos):
    left_row, left_col = crate_left_pos

    left_adj_row, left_adj_col = left_row, left_col - 1
    left_adj_cell = expanded_m[left_adj_row][left_adj_col]

    if left_adj_cell == ".":
        expanded_m[left_adj_row][left_adj_col] = "["
        expanded_m[left_adj_row][left_adj_col + 1] = "]"

        # expanded_m[left_row][left_col] = "."
    elif left_adj_cell == "]":
        move_left(expanded_m, (left_adj_row, left_adj_col - 1))
        expanded_m[left_adj_row][left_adj_col] = "["
        expanded_m[left_adj_row][left_adj_col + 1] = "]"

        # expanded_m[left_row][left_col] = "."
    else:
        raise Exception("invalid position moving left")


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

expanded_m = []
for i in range(len(m)):
    new_row = []
    for j in range(len(m[0])):
        cell = m[i][j]
        if cell == "#":
            new_row.append("#")
            new_row.append("#")
        elif cell == "O":
            new_row.append("[")
            new_row.append("]")
        elif cell == ".":
            new_row.append(".")
            new_row.append(".")
        elif cell == "@":
            new_row.append("@")
            new_row.append(".")
        else:
            raise Exception("invalid cell")

    expanded_m.append(new_row)

for inst in instrs:
    robot_pos = None
    for i in range(len(expanded_m)):
        for j in range(len(expanded_m[0])):
            if expanded_m[i][j] == "@":
                robot_pos = (i, j)
    robot_row, robot_col = robot_pos

    if inst == "^":
        above_row, above_col = robot_row - 1, robot_col
        above_cell = expanded_m[above_row][above_col]

        if above_cell == ".":
            expanded_m[above_row][above_col] = "@"
            expanded_m[robot_row][robot_col] = "."
        elif above_cell == "#":
            pass  # nothing happens, no move
        elif above_cell == "[":
            if can_move_vertical(expanded_m, (above_row, above_col), "^"):
                move_crate_vertical(expanded_m, (above_row, above_col), "^")
                expanded_m[above_row][above_col] = "@"
                expanded_m[robot_row][robot_col] = "."
        elif above_cell == "]":
            if can_move_vertical(expanded_m, (above_row, above_col - 1), "^"):
                move_crate_vertical(expanded_m, (above_row, above_col - 1), "^")
                expanded_m[above_row][above_col] = "@"
                expanded_m[robot_row][robot_col] = "."
        else:
            raise Exception("invalid cell going up")
    elif inst == ">":
        right_row, right_col = robot_row, robot_col + 1
        right_cell = expanded_m[right_row][right_col]

        if right_cell == ".":
            expanded_m[right_row][right_col] = "@"
            expanded_m[robot_row][robot_col] = "."
        elif right_cell == "#":
            pass  # nothing happens, no move
        elif right_cell == "[":
            if can_move_right(expanded_m, (right_row, right_col)):
                move_right(expanded_m, (right_row, right_col))
                expanded_m[right_row][right_col] = "@"
                expanded_m[robot_row][robot_col] = "."
        else:
            raise Exception("invalid cell going right " + right_cell)
    elif inst == "v":
        below_row, below_col = robot_row + 1, robot_col
        below_cell = expanded_m[below_row][below_col]

        if below_cell == ".":
            expanded_m[below_row][below_col] = "@"
            expanded_m[robot_row][robot_col] = "."
        elif below_cell == "#":
            pass  # nothing happens
        elif below_cell == "[":
            if can_move_vertical(expanded_m, (below_row, below_col), "v"):
                move_crate_vertical(expanded_m, (below_row, below_col), "v")
                expanded_m[below_row][below_col] = "@"
                expanded_m[robot_row][robot_col] = "."
        elif below_cell == "]":
            if can_move_vertical(expanded_m, (below_row, below_col - 1), "v"):
                move_crate_vertical(expanded_m, (below_row, below_col - 1), "v")
                expanded_m[below_row][below_col] = "@"
                expanded_m[robot_row][robot_col] = "."
        else:
            raise Exception("invalid cell going down " + below_cell)
    elif inst == "<":
        left_row, left_col = robot_row, robot_col - 1
        left_cell = expanded_m[left_row][left_col]

        if left_cell == ".":
            expanded_m[left_row][left_col] = "@"
            expanded_m[robot_row][robot_col] = "."
        elif left_cell == "#":
            pass  # nothing happens, no move
        elif left_cell == "]":
            if can_move_left(expanded_m, (left_row, left_col - 1)):
                move_left(expanded_m, (left_row, left_col - 1))
                expanded_m[left_row][left_col] = "@"
                expanded_m[robot_row][robot_col] = "."
        else:
            raise Exception("invalid cell going left " + left_cell)
    else:
        raise Exception("invalid instruction")


gps_sum = 0
for i in range(len(expanded_m)):
    for j in range(len(expanded_m[0])):
        if expanded_m[i][j] == "[":
            gps_sum += 100 * i + j

print(gps_sum)
