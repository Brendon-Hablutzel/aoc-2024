import re


def parse_mul_str(s: str) -> list[int]:
    s = s.lstrip("mul(")
    s = s.rstrip(")")
    return [int(a) for a in s.split(",")]


line = input()
pattern = r"mul\(\d+,\d+\)"

matches = re.findall(pattern, line)

summed = 0
for match in matches:
    [a, b] = parse_mul_str(match)
    summed += a * b

print(summed)
