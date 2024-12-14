import re

button_pattern = r"X\+(\d+), Y\+(\d+)"
prize_pattern = r"X\=(\d+), Y\=(\d+)"

games = []

while True:
    button_a_line = input()
    a_groups = re.search(button_pattern, button_a_line).groups()
    button_a_x = int(a_groups[0])
    button_a_y = int(a_groups[1])

    button_b_line = input()
    b_groups = re.search(button_pattern, button_b_line).groups()
    button_b_x = int(b_groups[0])
    button_b_y = int(b_groups[1])

    prize_line = input()
    prize_groups = re.search(prize_pattern, prize_line).groups()
    prize_x = int(prize_groups[0]) + 10000000000000
    prize_y = int(prize_groups[1]) + 10000000000000

    games.append(
        ((button_a_x, button_a_y), (button_b_x, button_b_y), (prize_x, prize_y))
    )

    try:
        input()  # empty line
    except EOFError:
        break


a_cost = 3
b_cost = 1


def cheapest_cost(button_a, button_b, target_pos):
    target_x, target_y = target_pos
    a_x, a_y = button_a
    b_x, b_y = button_b

    # use cramer's rule

    detA = a_x * b_y - b_x * a_y

    detAb1 = target_x * b_y - b_x * target_y

    detAb2 = a_x * target_y - a_y * target_x

    return [detAb1 / detA, detAb2 / detA]


total = 0
for game in games:
    button_a, button_b, prize_pos = game
    best = cheapest_cost(button_a, button_b, prize_pos)
    [best_a, best_b] = best
    if best_a == int(best_a) and best_b == int(best_b):
        total += (int(best_a) * a_cost) + (int(best_b) * b_cost)


print(total)
