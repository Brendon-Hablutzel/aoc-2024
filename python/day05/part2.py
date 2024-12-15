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


def check_is_valid(update):
    is_valid = True
    to_be_updated = set(update)
    for page in update:
        depends_on = dependencies[page] if page in dependencies else set()
        if len(to_be_updated.intersection(depends_on)) != 0:
            is_valid = False

        to_be_updated.remove(page)
    return is_valid


def check_has_dependencies_after(update, page_idx):
    page = update[page_idx]
    if page not in dependencies:
        return False

    page_dependencies = dependencies[page]
    for i in range(page_idx + 1, len(update)):
        after_page = update[i]
        if after_page in page_dependencies:
            return True

    return False


for update in updates:
    is_valid = True
    to_be_updated = set(update)
    for page in update:
        depends_on = dependencies[page] if page in dependencies else set()
        if len(to_be_updated.intersection(depends_on)) != 0:
            is_valid = False

        to_be_updated.remove(page)

    if not is_valid:
        original = update.copy()

        checks = True
        while checks:
            checks = False
            for i in range(len(update) - 1):
                if check_has_dependencies_after(update, i):
                    page = update.pop(i)
                    update.insert(i + 1, page)
                    checks = True

        if not check_is_valid(update):
            print(original, update)

        middle_val = get_middle_val(update)
        summed += middle_val


print(summed)
