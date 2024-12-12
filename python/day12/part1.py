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
    perimeter = 0
    for pos in region:
        row, col = pos
        if (row + 1, col) not in region:
            perimeter += 1
        if (row - 1, col) not in region:
            perimeter += 1
        if (row, col + 1) not in region:
            perimeter += 1
        if (row, col - 1) not in region:
            perimeter += 1

    total_price += area * perimeter

print(total_price)
