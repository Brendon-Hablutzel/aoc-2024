given = {}
to_resolve = {}

first_part = True
while True:
    try:
        line = input()

        if len(line) == 0:
            first_part = False
        elif first_part:
            [name, value] = line.split(": ")
            given[name] = int(value)
        else:
            [in_1, operation, in_2, _, out] = line.split(" ")

            to_resolve[out] = (in_1, in_2, operation)
    except EOFError:
        break


def resolve(wire):
    if wire in given:
        return given[wire]

    in_1, in_2, operation = to_resolve[wire]
    val_1 = resolve(in_1)
    val_2 = resolve(in_2)

    if operation == "AND":
        return val_1 & val_2
    elif operation == "OR":
        return val_1 | val_2
    elif operation == "XOR":
        return val_1 ^ val_2
    else:
        raise Exception("invalid operation")


total = 0
p = 0

for wire in sorted(to_resolve.keys()):
    val = resolve(wire)
    if wire.startswith("z"):
        total += val * 2**p
        p += 1

print(total)
