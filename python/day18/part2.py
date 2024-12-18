from heapq import heappush, heappop
import math

byte_positions = []

while True:
    try:
        line = input()
        # input is given as x, y, so switch to make it row, col
        byte_positions.append(list(reversed([int(d) for d in line.split(",")])))
    except EOFError:
        break

# hardcoded for real input (would need to be changed for sample)
mem_size = 71
falling_bytes = 1024

memory = array = [["." for _ in range(mem_size)] for _ in range(mem_size)]

for row, col in byte_positions[:falling_bytes]:
    memory[row][col] = "#"


def find_shortest(memory, start_pos, end_pos):
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
                or neighbor_row >= mem_size
                or neighbor_col < 0
                or neighbor_col >= mem_size
            ):
                continue

            neighbor_cell = memory[neighbor_row][neighbor_col]

            if neighbor_cell == "#":
                continue

            heappush(pq, (cost + 1, (neighbor_row, neighbor_col)))

    return best


for row, col in byte_positions[falling_bytes:]:
    memory[row][col] = "#"
    cost = find_shortest(memory, (0, 0), (mem_size - 1, mem_size - 1))
    if math.isinf(cost):
        print(f"{col},{row}")
        break
