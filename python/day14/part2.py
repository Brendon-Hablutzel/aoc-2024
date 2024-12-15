robots = []

while True:
    try:
        line = input()
        [position, velocity] = line.split()
        position = position.lstrip("p=")
        [p_x, p_y] = [int(d) for d in position.split(",")]

        velocity = velocity.lstrip("v=")
        [v_x, v_y] = [int(d) for d in velocity.split(",")]

        robots.append(((p_x, p_y), (v_x, v_y)))
    except EOFError:
        break

input_width = 101
input_height = 103


def show_robots(positions):
    board = [[" " for _ in range(input_width)] for _ in range(input_height)]

    for x, y in positions:
        cell = board[y][x]
        if cell == " ":
            board[y][x] = 1
        else:
            board[y][x] += 1

    for row in board:
        print("".join(str(c) for c in row))


def simulate_with_seconds(seconds):
    positions = []
    for robot in robots:
        position, velocity = robot
        p_x, p_y = position
        v_x, v_y = velocity

        final_x = (p_x + seconds * v_x) % input_width
        final_y = (p_y + seconds * v_y) % input_height
        positions.append((final_x, final_y))

    return positions


def compute_centrality(positions):
    center_x = input_width // 2
    center_y = input_height // 2

    total = 0
    for x, y in positions:
        x_dist = abs(x - center_x)
        y_dist = abs(y - center_y)
        total += 25 - x_dist + 25 - y_dist

    return total


for s in range(10_000):
    positions = simulate_with_seconds(s)

    centrality = compute_centrality(positions)

    if centrality > 5000:
        print(s)
        print(centrality)
        show_robots(positions)
        print("-" * input_width)
