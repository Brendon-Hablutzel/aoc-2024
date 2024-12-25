# NOTE: NOT A SOLUTION. This just contains some fragments to programmatically
# implement a combination of heuristic and brute force approaches

from itertools import combinations

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


bits_to_add = 45
x = []
y = []
result = []  # z00 first, then z01 ... up to and including z45
carry = 0
for i in range(bits_to_add):
    x_bit = given["x" + str(i).zfill(2)]
    x.append(x_bit)
    y_bit = given["y" + str(i).zfill(2)]
    y.append(y_bit)
    z_bit = x_bit ^ y_bit ^ carry
    result.append(z_bit)

    if (x_bit & y_bit) | (y_bit & carry) | (carry & x_bit):
        carry = 1
    else:
        carry = 0

    if i == bits_to_add - 1:
        result.append(carry)

print("".join(map(str, x)))
print("".join(map(str, y)))
print("".join(map(str, result)))


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

input_z = []
for wire in sorted(to_resolve.keys()):
    val = resolve(wire)
    if wire.startswith("z"):
        # print(wire)
        # print(val)
        input_z.append(val)
        # total += val * 2**p
        # p += 1

# print(total)
print("".join(map(str, input_z)))

# z06 has OR, z38 has AND, z45 has AND, z23 has AND
wrong = ["z06", "z38", "z45", "z23"]


def string_structure(wire):
    if wire in given:
        return wire

    in_1, in_2, operation = to_resolve[wire]
    val_1 = string_structure(in_1)
    val_2 = string_structure(in_2)

    if operation == "AND":
        return "(" + str(val_1) + " AND " + str(val_2) + ")"
    elif operation == "OR":
        return "(" + str(val_1) + " OR " + str(val_2) + ")"
    elif operation == "XOR":
        return "(" + str(val_1) + " XOR " + str(val_2) + ")"
    else:
        raise Exception("invalid operation")


# print("01", string_structure("z01"))
# print("02", string_structure("z02"))
# print("03", string_structure("z03"))
# print("04", string_structure("z04"))
# print("05", string_structure("z05"))
# print("06", string_structure("z06"))

for wire in to_resolve:
    in_1, in_2, operation = to_resolve[wire]
    if operation == "XOR" and (
        not (
            (
                (in_1.startswith("x") and in_2.startswith("y"))
                or (in_1.startswith("y") and in_2.startswith("x"))
            )
            or (wire.startswith("z"))
        )
    ):
        print("incorrect XOR", in_1, in_2, operation, wire)

    if wire.startswith("z") and operation != "XOR" and wire != "z45":
        print("missing XOR", in_1, in_2, operation, wire)


# print(string_structure("dhg"))
# dhg should swap with z06
# print(string_structure("bhd"))
# bhd should swap with z23
# print(string_structure("nbf"))
# nbf should swap with z38

print(",".join(sorted(["dhg", "bhd", "nbf", "z06", "z23", "z38", "dpd", "brk"])))


to_resolve["dhg"], to_resolve["z06"] = to_resolve["z06"], to_resolve["dhg"]
to_resolve["bhd"], to_resolve["z23"] = to_resolve["z23"], to_resolve["bhd"]
to_resolve["nbf"], to_resolve["z38"] = to_resolve["z38"], to_resolve["nbf"]

for wire_a, wire_b in combinations(to_resolve.keys(), 2):
    to_resolve[wire_a], to_resolve[wire_b] = to_resolve[wire_b], to_resolve[wire_a]

    bits_to_add = 45
    x = []
    y = []
    result = []  # z00 first, then z01 ... up to and including z45
    carry = 0
    for i in range(bits_to_add):
        x_bit = given["x" + str(i).zfill(2)]
        x.append(x_bit)
        y_bit = given["y" + str(i).zfill(2)]
        y.append(y_bit)
        z_bit = x_bit ^ y_bit ^ carry
        result.append(z_bit)

        if (x_bit & y_bit) | (y_bit & carry) | (carry & x_bit):
            carry = 1
        else:
            carry = 0

        if i == bits_to_add - 1:
            result.append(carry)

    # print("".join(map(str, x)))
    # print("".join(map(str, y)))
    # print("".join(map(str, result)))

    input_z = []
    for wire in sorted(to_resolve.keys()):
        try:
            val = resolve(wire)
        except RecursionError:
            break
        if wire.startswith("z"):
            # print(wire)
            # print(val)
            input_z.append(val)
            # total += val * 2**p
            # p += 1

    # print(total)
    # print("".join(map(str, input_z)))
    if "".join(map(str, result)) == "".join(map(str, input_z)):
        print("found", wire_a, wire_b)

    to_resolve[wire_a], to_resolve[wire_b] = to_resolve[wire_b], to_resolve[wire_a]
