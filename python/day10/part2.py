from collections import deque

m = []

while True:
    try:
        line = input()
        vals = [int(c) for c in line]

        m.append(vals)
    except EOFError:
        break

starting_positions = []
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] == 0:
            starting_positions.append((i, j))


def find_trails(start_pos):
    nines = []

    q = deque()
    q.append(start_pos)
    while len(q) > 0:
        pos = q.popleft()

        pos_row, pos_col = pos
        pos_value = m[pos_row][pos_col]

        if pos_value == 9:
            nines.append(pos)
            continue

        neighbors = [
            (pos_row + 1, pos_col),
            (pos_row - 1, pos_col),
            (pos_row, pos_col + 1),
            (pos_row, pos_col - 1),
        ]
        for neighbor in neighbors:
            neighbor_row, neighbor_col = neighbor
            if (
                neighbor_row >= 0
                and neighbor_row < len(m)
                and neighbor_col >= 0
                and neighbor_col < len(m[0])
            ):
                neighbor_value = m[neighbor_row][neighbor_col]
                if neighbor_value - 1 == pos_value:
                    q.append(neighbor)

    return nines


total = sum(len(find_trails(start)) for start in starting_positions)

print(total)
