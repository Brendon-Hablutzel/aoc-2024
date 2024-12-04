word_search = []

while True:
    try:
        line = input()
    except EOFError:
        break

    word_search.append(list(line))

dim = len(word_search)


def get_letter_or_none(i, j):
    return (
        word_search[i][j]
        if i >= 0 and i <= dim - 1 and j >= 0 and j <= dim - 1
        else None
    )


def check_diagonal_up_left(i, j):
    first = get_letter_or_none(i, j)
    second = get_letter_or_none(i - 1, j - 1)
    third = get_letter_or_none(i - 2, j - 2)
    fourth = get_letter_or_none(i - 3, j - 3)
    return first == "X" and second == "M" and third == "A" and fourth == "S"


def check_diagonal_up_right(i, j):
    first = get_letter_or_none(i, j)
    second = get_letter_or_none(i - 1, j + 1)
    third = get_letter_or_none(i - 2, j + 2)
    fourth = get_letter_or_none(i - 3, j + 3)
    return first == "X" and second == "M" and third == "A" and fourth == "S"


def check_diagonal_down_left(i, j):
    first = get_letter_or_none(i, j)
    second = get_letter_or_none(i + 1, j - 1)
    third = get_letter_or_none(i + 2, j - 2)
    fourth = get_letter_or_none(i + 3, j - 3)
    return first == "X" and second == "M" and third == "A" and fourth == "S"


def check_diagonal_down_right(i, j):
    first = get_letter_or_none(i, j)
    second = get_letter_or_none(i + 1, j + 1)
    third = get_letter_or_none(i + 2, j + 2)
    fourth = get_letter_or_none(i + 3, j + 3)
    return first == "X" and second == "M" and third == "A" and fourth == "S"


def check_left(i, j):
    first = get_letter_or_none(i, j)
    second = get_letter_or_none(i, j - 1)
    third = get_letter_or_none(i, j - 2)
    fourth = get_letter_or_none(i, j - 3)
    return first == "X" and second == "M" and third == "A" and fourth == "S"


def check_right(i, j):
    first = get_letter_or_none(i, j)
    second = get_letter_or_none(i, j + 1)
    third = get_letter_or_none(i, j + 2)
    fourth = get_letter_or_none(i, j + 3)
    return first == "X" and second == "M" and third == "A" and fourth == "S"


def check_up(i, j):
    first = get_letter_or_none(i, j)
    second = get_letter_or_none(i - 1, j)
    third = get_letter_or_none(i - 2, j)
    fourth = get_letter_or_none(i - 3, j)
    return first == "X" and second == "M" and third == "A" and fourth == "S"


def check_down(i, j):
    first = get_letter_or_none(i, j)
    second = get_letter_or_none(i + 1, j)
    third = get_letter_or_none(i + 2, j)
    fourth = get_letter_or_none(i + 3, j)
    return first == "X" and second == "M" and third == "A" and fourth == "S"


total = 0
for i in range(dim):
    for j in range(dim):
        if check_diagonal_down_left(i, j):
            total += 1

        if check_diagonal_down_right(i, j):
            total += 1

        if check_diagonal_up_left(i, j):
            total += 1

        if check_diagonal_up_right(i, j):
            total += 1

        if check_left(i, j):
            total += 1

        if check_right(i, j):
            total += 1

        if check_up(i, j):
            total += 1

        if check_down(i, j):
            total += 1

print(total)
