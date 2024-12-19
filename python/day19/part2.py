patterns = input().split(", ")

input()

desired_designs = []

while True:
    try:
        desired_designs.append(input())
    except EOFError:
        break


def num_ways_possible(design):
    ans = [0 for _ in range(len(design))]

    for i in range(len(design)):
        for pattern in patterns:
            design_component = design[i - len(pattern) + 1 : i + 1]
            if pattern == design_component:
                ans[i] += ans[i - len(pattern)] if i - len(pattern) >= 0 else 1

    return ans[-1]


total_possible_ways = sum(num_ways_possible(design) for design in desired_designs)

print(total_possible_ways)
