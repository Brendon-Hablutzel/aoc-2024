disk = list(input())


def find_next_open_chunk(expanded_disk, end_idx_exclusive, size):
    i = 0
    while i + size <= end_idx_exclusive:
        window = expanded_disk[i : i + size]
        if all(b == "." for b in window):
            return i
        i += 1
    return None


def compute_checksum(expanded_disk):
    return sum(
        expanded_disk[i] * i
        for i in range(len(expanded_disk))
        if expanded_disk[i] != "."
    )


expanded_disk = list()
current_id = 0
for i, block in enumerate(disk):
    block_val = int(block)
    if i % 2 == 0:
        for _ in range(block_val):
            expanded_disk.append(current_id)
        current_id += 1
    else:
        for _ in range(block_val):
            expanded_disk.append(".")


current_id -= 1  # the largest id
idx = len(expanded_disk) - 1
size = 0
while current_id >= 0:
    block = expanded_disk[idx]

    if block == ".":
        if size == 0:
            idx -= 1
        else:
            first_open_idx = find_next_open_chunk(expanded_disk, idx + 1, size)
            if first_open_idx is not None:
                for i in range(size):
                    expanded_disk[idx + 1 + i] = "."
                for i in range(size):
                    expanded_disk[first_open_idx + i] = current_id
            current_id -= 1
            size = 0
    else:
        if block == current_id:
            size += 1
            idx -= 1
        else:
            if size == 0:
                idx -= 1
            else:
                first_open_idx = find_next_open_chunk(expanded_disk, idx + 1, size)
                if first_open_idx is not None:
                    for i in range(size):
                        expanded_disk[idx + 1 + i] = "."
                    for i in range(size):
                        expanded_disk[first_open_idx + i] = current_id
                current_id -= 1
                size = 0


print(compute_checksum(expanded_disk))
