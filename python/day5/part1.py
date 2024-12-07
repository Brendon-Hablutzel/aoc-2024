def get_middle_val(updates):
    middle_idx = len(updates) // 2
    return updates[middle_idx]


updates = []
dependencies = {}  # page -> set of pages it's dependent on (pages that must be printed first)

first_section = True
while True:
    try:
        line = input()
    except EOFError:
        break

    if len(line) == 0:
        first_section = False
        continue

    if first_section:
        [before, after] = [int(p) for p in line.split("|")]
        if after in dependencies:
            dependencies[after].add(before)
        else:
            dependencies[after] = {before}
    else:
        updates.append([int(p) for p in line.split(",")])

summed = 0

for update in updates:
    is_valid = True
    to_be_updated = set(update)
    for page in update:
        depends_on = dependencies[page] if page in dependencies else set()
        if len(to_be_updated.intersection(depends_on)) != 0:
            is_valid = False

        to_be_updated.remove(page)

    if is_valid:
        summed += get_middle_val(update)

print(summed)
