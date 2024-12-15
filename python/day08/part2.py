from collections import defaultdict

m = []

while True:
    try:
        line = input()
    except EOFError:
        break

    m.append(list(line))


antennas = defaultdict(list)

for row_idx in range(len(m)):
    for col_idx in range(len(m[0])):
        cell = m[row_idx][col_idx]
        if cell != ".":
            antennas[cell].append((row_idx, col_idx))


antinodes = set()
for freq, locations in antennas.items():
    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            row1, col1 = locations[i]
            row2, col2 = locations[j]

            row_dist = abs(row2 - row1)
            col_dist = abs(col2 - col1)

            # find negative multiples
            c = 0
            while True:
                new_row = row1 + (row_dist * c)
                if (row1 > row2 and col1 > col2) or (row2 > row1 and col2 > col1):
                    new_col = col1 + (col_dist * c)
                else:
                    new_col = col1 - (col_dist * c)

                if (
                    new_row < 0
                    or new_row >= len(m)
                    or new_col < 0
                    or new_col >= len(m[0])
                ):
                    break

                antinodes.add((new_row, new_col))

                c -= 1

            # find positive multiples
            c = 0
            while True:
                new_row = row1 + (row_dist * c)
                if (row1 > row2 and col1 > col2) or (row2 > row1 and col2 > col1):
                    new_col = col1 + (col_dist * c)
                else:
                    new_col = col1 - (col_dist * c)

                if (
                    new_row < 0
                    or new_row >= len(m)
                    or new_col < 0
                    or new_col >= len(m[0])
                ):
                    break

                antinodes.add((new_row, new_col))

                c += 1

print(len(antinodes))
