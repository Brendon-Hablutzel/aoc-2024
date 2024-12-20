from heapq import heappush, heappop
from itertools import combinations

m = []

while True:
    try:
        line = input()
        m.append(list(line))
    except EOFError:
        break

m_rows = len(m)
m_cols = len(m[0])

start_pos = None
end_pos = None
for i in range(m_rows):
    for j in range(m_cols):
        if m[i][j] == "S":
            start_pos = (i, j)
        elif m[i][j] == "E":
            end_pos = (i, j)


def solve(m):
    pq = []

    heappush(pq, (0, start_pos))

    costs = {}

    while len(pq) > 0:
        cost, pos = heappop(pq)
        row, col = pos

        if pos in costs and costs[pos] <= cost:
            continue

        costs[pos] = cost

        if pos == end_pos:
            continue

        for row_diff, col_diff in [
            (-1, 0),  # up
            (0, 1),  # right
            (1, 0),  # down
            (0, -1),  # left
        ]:
            neighbor_row = row + row_diff
            neighbor_col = col + col_diff

            if (
                neighbor_row < 0
                or neighbor_row >= m_rows
                or neighbor_col < 0
                or neighbor_col >= m_cols
            ):
                continue

            neighbor_cell = m[neighbor_row][neighbor_col]

            if neighbor_cell == "#":
                continue

            heappush(pq, (cost + 1, (neighbor_row, neighbor_col)))

    return costs


found_costs = solve(m)

save_at_least_100 = 0
for a, b in combinations(found_costs.items(), 2):
    # for all possible pairs of points that aren't walls, check if the
    # shortest possible valid cheat would save at least 100 picoseconds
    a_pos, a_cost = a
    a_row, a_col = a_pos

    b_pos, b_cost = b
    b_row, b_col = b_pos

    taxicab_dist = abs(a_row - b_row) + abs(a_col - b_col)

    cheated_cost = a_cost + taxicab_dist
    if taxicab_dist <= 20 and b_cost - cheated_cost >= 100:
        save_at_least_100 += 1

print(save_at_least_100)
