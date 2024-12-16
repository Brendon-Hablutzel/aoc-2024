from heapq import heappush, heappop

maze = []

while True:
    try:
        line = input()

        maze.append(list(line))
    except EOFError:
        break


maze_rows = len(maze)
maze_cols = len(maze[0])

start_pos = None
end_pos = None
for i in range(maze_rows):
    for j in range(maze_cols):
        if maze[i][j] == "S":
            start_pos = (i, j)
        elif maze[i][j] == "E":
            end_pos = (i, j)


def bfs(maze):
    pq = []
    # position, orientation, score
    heappush(pq, (0, start_pos, ">"))

    # stores a mapping of (position, orientation) -> minimum cost found
    # to get to that position in that orientation so far
    costs = {}

    best_cost = float("inf")

    while len(pq) > 0:
        current_cost, pos, orientation = heappop(pq)
        row, col = pos

        if pos == end_pos:
            if current_cost < best_cost:
                best_cost = current_cost
            continue

        if (pos, orientation) in costs and costs[(pos, orientation)] <= current_cost:
            continue

        costs[(pos, orientation)] = current_cost

        up_row, up_col = row - 1, col
        up_cell = maze[up_row][up_col]
        if up_cell != "#":
            rotation_cost = 0
            if orientation == "<" or orientation == ">":
                rotation_cost = 1000
            elif orientation == "v":
                rotation_cost = 1000 * 2

            heappush(pq, (current_cost + rotation_cost + 1, (up_row, up_col), "^"))

        right_row, right_col = row, col + 1
        right_cell = maze[right_row][right_col]
        if right_cell != "#":
            rotation_cost = 0
            if orientation == "^" or orientation == "v":
                rotation_cost = 1000
            elif orientation == "<":
                rotation_cost = 1000 * 2

            heappush(
                pq, (current_cost + rotation_cost + 1, (right_row, right_col), ">")
            )

        down_row, down_col = row + 1, col
        down_cell = maze[down_row][down_col]
        if down_cell != "#":
            rotation_cost = 0
            if orientation == "<" or orientation == ">":
                rotation_cost = 1000
            elif orientation == "^":
                rotation_cost = 1000 * 2

            heappush(pq, (current_cost + rotation_cost + 1, (down_row, down_col), "v"))

        left_row, left_col = row, col - 1
        left_cell = maze[left_row][left_col]
        if left_cell != "#":
            rotation_cost = 0
            if orientation == "^" or orientation == "v":
                rotation_cost = 1000
            elif orientation == ">":
                rotation_cost = 1000 * 2

            heappush(pq, (current_cost + rotation_cost + 1, (left_row, left_col), "<"))

    return best_cost


best_cost = bfs(maze)
print(best_cost)
