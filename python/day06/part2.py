import copy

original_m = []


while True:
    try:
        line = input()
    except EOFError:
        break

    original_m.append(list(line))


def check_loop(m):
    def get_or_none(row_idx, col_idx):
        return (
            m[row_idx][col_idx]
            if row_idx >= 0
            and row_idx < len(m)
            and col_idx >= 0
            and col_idx < len(m[0])
            else None
        )

    pos_to_orientation = {}

    current_guard_pos = (None, None)

    for row_idx in range(len(m)):
        row = m[row_idx]
        for col_idx in range(len(row)):
            cell = row[col_idx]
            if cell == "^":
                current_guard_pos = (row_idx, col_idx)

    while True:
        guard_row_idx, guard_col_idx = current_guard_pos
        guard = m[guard_row_idx][guard_col_idx]

        if guard == "^":
            cell_above = get_or_none(guard_row_idx - 1, guard_col_idx)
            if cell_above is None:
                m[guard_row_idx][guard_col_idx] = "X"
                break

            if cell_above == "#":
                m[guard_row_idx][guard_col_idx] = ">"
            else:
                if (
                    current_guard_pos in pos_to_orientation
                    and pos_to_orientation[current_guard_pos] == guard
                ):
                    return True
                pos_to_orientation[current_guard_pos] = m[guard_row_idx][guard_col_idx]
                m[guard_row_idx][guard_col_idx] = "X"
                m[guard_row_idx - 1][guard_col_idx] = "^"
                current_guard_pos = (guard_row_idx - 1, guard_col_idx)
        elif guard == ">":
            cell_right = get_or_none(guard_row_idx, guard_col_idx + 1)
            if cell_right is None:
                m[guard_row_idx][guard_col_idx] = "X"
                break

            if cell_right == "#":
                m[guard_row_idx][guard_col_idx] = "$"
            else:
                if (
                    current_guard_pos in pos_to_orientation
                    and pos_to_orientation[current_guard_pos] == guard
                ):
                    return True
                pos_to_orientation[current_guard_pos] = m[guard_row_idx][guard_col_idx]
                m[guard_row_idx][guard_col_idx] = "X"
                m[guard_row_idx][guard_col_idx + 1] = ">"
                current_guard_pos = (guard_row_idx, guard_col_idx + 1)
        elif guard == "$":
            cell_down = get_or_none(guard_row_idx + 1, guard_col_idx)
            if cell_down is None:
                m[guard_row_idx][guard_col_idx] = "X"
                break

            if cell_down == "#":
                m[guard_row_idx][guard_col_idx] = "<"
            else:
                if (
                    current_guard_pos in pos_to_orientation
                    and pos_to_orientation[current_guard_pos] == guard
                ):
                    return True
                pos_to_orientation[current_guard_pos] = m[guard_row_idx][guard_col_idx]
                m[guard_row_idx][guard_col_idx] = "X"
                m[guard_row_idx + 1][guard_col_idx] = "$"
                current_guard_pos = (guard_row_idx + 1, guard_col_idx)
        elif guard == "<":
            cell_left = get_or_none(guard_row_idx, guard_col_idx - 1)
            if cell_left is None:
                m[guard_row_idx][guard_col_idx] = "X"
                break

            if cell_left == "#":
                m[guard_row_idx][guard_col_idx] = "^"
            else:
                if (
                    current_guard_pos in pos_to_orientation
                    and pos_to_orientation[current_guard_pos] == guard
                ):
                    return True
                pos_to_orientation[current_guard_pos] = m[guard_row_idx][guard_col_idx]
                m[guard_row_idx][guard_col_idx] = "X"
                m[guard_row_idx][guard_col_idx - 1] = "<"
                current_guard_pos = (guard_row_idx, guard_col_idx - 1)
        else:
            raise Exception("bad guard", guard)

    return False


current_guard_pos = (None, None)

for row_idx in range(len(original_m)):
    row = original_m[row_idx]
    for col_idx in range(len(row)):
        cell = row[col_idx]
        if cell == "^":
            current_guard_pos = (row_idx, col_idx)


loops = 0
for row_idx in range(len(original_m)):
    for col_idx in range(len(original_m[0])):
        cell = original_m[row_idx][col_idx]
        if cell != "#" and cell != "^":
            new = copy.deepcopy(original_m)
            new[row_idx][col_idx] = "#"
            if check_loop(new):
                loops += 1

print(loops)
