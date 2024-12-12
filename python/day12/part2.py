from collections import deque

gardens = []

while True:
    try:
        gardens.append(list(input()))
    except EOFError:
        break


def get_region(start_pos):
    visited = set()
    start_row, start_col = start_pos
    start_region = gardens[start_row][start_col]

    region = set()

    q = deque()
    q.append(start_pos)
    while len(q) > 0:
        current_pos = q.popleft()
        current_row, current_col = current_pos
        if (
            current_row < 0
            or current_row >= len(gardens)
            or current_col < 0
            or current_col >= len(gardens[0])
        ):
            continue

        if current_pos in visited:
            continue
        visited.add(current_pos)

        current_region = gardens[current_row][current_col]
        if current_region == start_region:
            region.add(current_pos)
            q.append((current_row + 1, current_col))
            q.append((current_row - 1, current_col))
            q.append((current_row, current_col + 1))
            q.append((current_row, current_col - 1))

    return region


regions = []
all_reached_points = set()
for i in range(len(gardens)):
    for j in range(len(gardens[0])):
        pos = (i, j)
        if pos in all_reached_points:
            continue

        region = get_region((i, j))
        all_reached_points = all_reached_points.union(region)
        regions.append(region)


total_price = 0
for region in regions:
    area = len(region)
    sides = 0
    n_corners = 0
    for pos in region:
        row, col = pos
        left = (row, col - 1)
        up = (row - 1, col)
        right = (row, col + 1)
        down = (row + 1, col)

        left_up = (row - 1, col - 1)
        left_down = (row + 1, col - 1)
        right_up = (row - 1, col + 1)
        right_down = (row + 1, col + 1)

        top_left = (row - 0.5, col - 0.5)
        if (left not in region and up not in region) or (
            up in region and left in region and left_up not in region
        ):
            n_corners += 1

        top_right = (row - 0.5, col + 0.5)
        if (up not in region and right not in region) or (
            up in region and right in region and right_up not in region
        ):
            n_corners += 1

        bottom_left = (row + 0.5, col - 0.5)
        if (left not in region and down not in region) or (
            left in region and down in region and left_down not in region
        ):
            n_corners += 1

        bottom_right = (row + 0.5, col + 0.5)
        if (down not in region and right not in region) or (
            down in region and right in region and right_down not in region
        ):
            n_corners += 1

    total_price += area * (n_corners)

print(total_price)
