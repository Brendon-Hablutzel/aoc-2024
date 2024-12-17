register_a = int(input()[len("Register A: ") :])
register_b = int(input()[len("Register B: ") :])
register_c = int(input()[len("Register C: ") :])

input()

instructions = list(map(int, input()[len("Program: ") :].split(",")))
instructions_str = ",".join(map(str, instructions))


def compute(instructions, register_a, register_b, register_c):
    def get_combo_value(combo_arg):
        if combo_arg >= 0 and combo_arg <= 3:
            # Combo operands 0 through 3 represent literal values 0 through 3.
            return combo_arg
        elif combo_arg == 4:
            # Combo operand 4 represents the value of register A.
            return register_a
        elif combo_arg == 5:
            # Combo operand 5 represents the value of register B.
            return register_b
        elif combo_arg == 6:
            # Combo operand 6 represents the value of register C.
            return register_c
        else:
            # Combo operand 7 is reserved and will not appear in valid programs.
            raise Exception("invalid combo arg " + combo_arg)

    output = []

    ip = 0
    while ip < len(instructions):
        inst = instructions[ip]
        arg = instructions[ip + 1]

        if inst == 0:
            # The adv instruction (opcode 0) performs division. The numerator is the
            # value in the A register. The denominator is found by raising 2 to the power
            # of the instruction's combo operand. (So, an operand of 2 would divide A by
            # 4 (2^2); an operand of 5 would divide A by 2^B.) The result of the division
            # operation is truncated to an integer and then written to the A register.
            numerator = register_a
            denominator = 2 ** get_combo_value(arg)
            register_a = numerator // denominator
        elif inst == 1:
            # The bxl instruction (opcode 1) calculates the bitwise XOR of register B and
            # the instruction's literal operand, then stores the result in register B.
            register_b = register_b ^ arg
        elif inst == 2:
            # The bst instruction (opcode 2) calculates the value of its combo operand
            # modulo 8 (thereby keeping only its lowest 3 bits), then writes that value
            # to the B register.
            register_b = get_combo_value(arg) % 8
        elif inst == 3:
            # The jnz instruction (opcode 3) does nothing if the A register is 0. However,
            # if the A register is not zero, it jumps by setting the instruction pointer
            # to the value of its literal operand; if this instruction jumps, the instruction
            # pointer is not increased by 2 after this instruction.
            if register_a != 0:
                ip = arg
                continue
        elif inst == 4:
            # The bxc instruction (opcode 4) calculates the bitwise XOR of register B and
            # register C,  then stores the result in register B. (For legacy reasons, this
            # instruction reads an operand but ignores it.)
            register_b = register_b ^ register_c
        elif inst == 5:
            # The out instruction (opcode 5) calculates the value of its combo operand modulo 8,
            # then outputs that value. (If a program outputs multiple values, they are separated
            # by commas.)
            res = get_combo_value(arg) % 8
            output.append(res)
        elif inst == 6:
            # The bdv instruction (opcode 6) works exactly like the adv instruction except that
            # the result is stored in the B register. (The numerator is still read from the A
            # register.)
            numerator = register_a
            denominator = 2 ** get_combo_value(arg)
            register_b = numerator // denominator
        elif inst == 7:
            # The cdv instruction (opcode 7) works exactly like the adv instruction except that the
            # result is stored in the C register. (The numerator is still read from the A register.)
            numerator = register_a
            denominator = 2 ** get_combo_value(arg)
            register_c = numerator // denominator
        else:
            raise Exception("invalid instruction " + inst)

        ip += 2

    return output


# NOTE: the length of the output is floor(log base 8 of a) + 1, so it must be
# somewhere between 8**15 and 8**16 - 1, since my input has 16 instructions.
# Then, if we just compute output for every possible a, notice that the nth digit
# of output changes every 8**n increments of a. Therefore, perform a backtracking search
# where we try to find the number in the form x1 * 8**15 + x2 * 8**14 + ..., finding
# each coefficient from largest (15) to smallest (0), each each coefficient changes the
# output digit of its index (i.e. changing x1 in x1 * 8**15 changes instructions[15])


# converts a base 8 representation to a typical base 10 integer
def get_number(coeffs):
    val = 0
    coeff_pow = 15
    for coeff in coeffs:
        val += coeff * 8**coeff_pow
        coeff_pow -= 1

    return val


found = []


def find_number(chosen_coeffs, current_significance):
    if current_significance < 0:
        found.append(chosen_coeffs)
        return

    for i in range(8):
        # try adding i * 8**current_significance, this gets base 8 representation
        new_coeffs = chosen_coeffs + [i]

        # convert the base 8 representation to the typical base 10 representation
        val = get_number(new_coeffs)
        if val == 0:
            continue

        # compute the output, if register a is given by 'val'
        computed = compute(instructions, val, register_b, register_c)

        # if the output value we are trying to affect matches the original instruction
        # at that index, then we can move on to finding the next least significant coefficient
        if computed[current_significance] == instructions[current_significance]:
            find_number(new_coeffs, current_significance - 1)


find_number([], 15)

print(get_number(found[0]))
