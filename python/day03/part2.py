import re


def parse_mul_str(s: str) -> list[int]:
    s = s.lstrip("mul(")
    s = s.rstrip(")")
    return [int(a) for a in s.split(",")]


line = input()
pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"

matches = re.findall(pattern, line)

summed = 0
enabled = True
for match in matches:
    print(match)
    if match == "do()":
        enabled = True
    elif match == "don't()":
        enabled = False
    elif enabled:
        [a, b] = parse_mul_str(match)
        summed += a * b

print(summed)
