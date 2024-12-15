memo = {}


def compute_stones_outputted(stone, blinks):
    if blinks == 0:
        return 1

    if (stone, blinks) in memo:
        return memo[(stone, blinks)]

    val = None
    if stone == 0:
        val = compute_stones_outputted(1, blinks - 1)
    elif len(str(stone)) % 2 == 0:
        stone_str = str(stone)
        halfway_idx = len(stone_str) // 2
        first_half = stone_str[:halfway_idx]
        second_half = stone_str[halfway_idx:]
        val = compute_stones_outputted(
            int(first_half), blinks - 1
        ) + compute_stones_outputted(int(second_half), blinks - 1)
    else:
        val = compute_stones_outputted(2024 * stone, blinks - 1)

    memo[(stone, blinks)] = val
    return val


stones = [int(stone) for stone in input().split()]

total = sum(compute_stones_outputted(stone, 75) for stone in stones)

print(total)
