patterns = input().split(", ")

input()

desired_designs = []

while True:
    try:
        desired_designs.append(input())
    except EOFError:
        break


def is_design_possible(design):
    possible = False

    def helper(design):
        nonlocal possible

        if possible:
            return

        if len(design) == 0:
            possible = True
            return

        for pattern in patterns:
            if design.startswith(pattern):
                helper(design[len(pattern) :])

    helper(design)
    return possible


num_possible = [is_design_possible(design) for design in desired_designs].count(True)

print(num_possible)
