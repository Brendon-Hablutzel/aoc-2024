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

            if row1 > row2 and col1 > col2:
                # loc1 is right and down from loc2
                a1col = col2 - col_dist
                a1row = row2 - row_dist

                a2col = col1 + col_dist
                a2row = row1 + row_dist
            elif row2 > row1 and col2 > col1:
                # loc2 is right and down from loc1
                a1col = col1 - col_dist
                a1row = row1 - row_dist

                a2col = col2 + col_dist
                a2row = row2 + row_dist
            elif row1 > row2 and col2 > col1:
                # loc1 is left and below loc2
                a1col = col1 - col_dist
                a1row = row1 + row_dist

                a2col = col2 + col_dist
                a2row = row2 - row_dist
            elif row2 > row1 and col1 > col2:
                # loc2 is left and below loc1
                a1col = col2 - col_dist
                a1row = row2 + row_dist

                a2col = col1 + col_dist
                a2row = row1 - row_dist
            else:
                raise Exception("invalid point config--should be unreachable")

            if a1row >= 0 and a1row < len(m) and a1col >= 0 and a1col < len(m[0]):
                antinodes.add((a1row, a1col))
                m[a1row][a1col] = "#"
            if a2row >= 0 and a2row < len(m) and a2col >= 0 and a2col < len(m[0]):
                antinodes.add((a2row, a2col))
                m[a2row][a2col] = "#"

print(len(antinodes))
