from heapq import heappush, heappop

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

    best = float("inf")

    costs = {}

    while len(pq) > 0:
        cost, pos = heappop(pq)
        row, col = pos

        if pos == end_pos:
            if cost < best:
                best = cost
            continue

        if pos in costs and costs[pos] <= cost:
            continue

        costs[pos] = cost

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

    return best


original_best = solve(m)

at_least_100 = 0

# NOTE: slow (~44s)

for i in range(1, m_rows - 1):
    for j in range(1, m_cols - 1):
        # heuristic to try and cut down on number of cheats that need to be checked--this only
        # performs a cheat when the bypassed wall is between two paths
        if m[i][j] == "#" and (
            (m[i + 1][j] != "#" and m[i - 1][j] != "#")
            or (m[i][j + 1] != "#" and m[i][j - 1] != "#")
        ):
            m[i][j] = "."
            new_best = solve(m)
            if original_best - new_best >= 100:
                at_least_100 += 1
            m[i][j] = "#"

print(at_least_100)
