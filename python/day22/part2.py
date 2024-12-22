import math
from collections import defaultdict

nums = []

while True:
    try:
        line = input()
        nums.append(int(line))
    except EOFError:
        break


def transform(n):
    n = (n ^ (n * 64)) % 16777216
    n = (n ^ math.floor(n / 32)) % 16777216
    n = (n ^ (n * 2048)) % 16777216
    return n


def get_2000_prices(initial):
    prices = []
    for _ in range(2000):
        prices.append(initial % 10)
        initial = transform(initial)
    return prices


def compute_results_map(initial, results):
    prices = get_2000_prices(initial)
    bought = set()
    for i in range(1, len(prices) - 3):
        # `i` is the start index of the current window
        diffs = (
            prices[i] - prices[i - 1],
            prices[i + 1] - prices[i],
            prices[i + 2] - prices[i + 1],
            prices[i + 3] - prices[i + 2],
        )
        next_price = prices[i + 3]

        if diffs not in bought:
            results[diffs] += next_price
            bought.add(diffs)


results = defaultdict(int)

for num in nums:
    compute_results_map(num, results)

best_change_sequence = max(results, key=results.get)
max_result = results[best_change_sequence]

print(max_result)
