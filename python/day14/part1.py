from collections import defaultdict

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

sample_width = 11
sample_height = 7

input_width = 101
input_height = 103

sim_seconds = 100


def get_quadrant(pos, height, width):
    x, y = pos
    midpoint_x = width // 2
    midpoint_y = height // 2
    if x == midpoint_x or y == midpoint_y:
        return None

    if x < midpoint_x and y < midpoint_y:
        return 1

    if x < midpoint_x and y > midpoint_y:
        return 2

    if x > midpoint_x and y < midpoint_y:
        return 3

    if x > midpoint_x and y > midpoint_y:
        return 4


quadrants = defaultdict(int)

for robot in robots:
    position, velocity = robot
    p_x, p_y = position
    v_x, v_y = velocity

    final_x = (p_x + sim_seconds * v_x) % input_width
    final_y = (p_y + sim_seconds * v_y) % input_height

    quad = get_quadrant((final_x, final_y), input_height, input_width)
    if quad is not None:
        quadrants[quad] += 1

total = 1
for n in quadrants.values():
    total *= n

print(total)
