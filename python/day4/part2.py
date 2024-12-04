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


def check_x_mas(i, j):
    upper_left = get_letter_or_none(i - 1, j - 1)
    upper_right = get_letter_or_none(i - 1, j + 1)
    lower_left = get_letter_or_none(i + 1, j - 1)
    lower_right = get_letter_or_none(i + 1, j + 1)

    middle = get_letter_or_none(i, j)
    if middle != "A":
        return False

    diagonal_one = (upper_left == "M" and lower_right == "S") or (
        upper_left == "S" and lower_right == "M"
    )
    diagonal_two = (upper_right == "M" and lower_left == "S") or (
        upper_right == "S" and lower_left == "M"
    )

    return diagonal_one and diagonal_two


total = 0
for i in range(dim):
    for j in range(dim):
        if check_x_mas(i, j):
            total += 1

print(total)
