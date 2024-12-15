disk = list(input())

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


checksum = 0

pos_idx = 0
back_idx = len(expanded_disk) - 1

while pos_idx <= back_idx:
    current_block = expanded_disk[pos_idx]
    back_block = expanded_disk[back_idx]

    if current_block == ".":
        if back_block != ".":
            checksum += pos_idx * back_block
            pos_idx += 1
        back_idx -= 1
    else:
        if back_block == ".":
            back_idx -= 1

        checksum += pos_idx * current_block
        pos_idx += 1

print(checksum)
