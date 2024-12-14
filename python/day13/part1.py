import re
import math

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
    prize_x = int(prize_groups[0])
    prize_y = int(prize_groups[1])

    games.append(
        ((button_a_x, button_a_y), (button_b_x, button_b_y), (prize_x, prize_y))
    )

    try:
        input()  # empty line

    except EOFError:
        break


a_cost = 3
b_cost = 1

memo = {}


def cheapest_cost(button_a, button_b, target_pos):
    target_x, target_y = target_pos
    if target_x < 0 or target_y < 0:
        return float("inf")

    a_x, a_y = button_a
    b_x, b_y = button_b

    if target_x == 0 and target_y == 0:
        return 0

    if target_pos in memo:
        return memo[target_pos]

    minimum = min(
        a_cost + cheapest_cost(button_a, button_b, (target_x - a_x, target_y - a_y)),
        b_cost + cheapest_cost(button_a, button_b, (target_x - b_x, target_y - b_y)),
    )

    memo[target_pos] = minimum

    return minimum


total = 0
for game in games:
    button_a, button_b, prize_pos = game
    best = cheapest_cost(button_a, button_b, prize_pos)
    memo = {}
    total += best if math.isfinite(best) else 0

print(total)
