import math

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


def compute_2000_secret_num(initial):
    for _ in range(2000):
        initial = transform(initial)
    return initial


total = sum(compute_2000_secret_num(n) for n in nums)
print(total)
