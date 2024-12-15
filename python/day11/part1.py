def blink_transform(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            halfway_idx = len(stone_str) // 2
            first_half = stone_str[:halfway_idx]
            second_half = stone_str[halfway_idx:]
            new_stones.append(int(first_half))
            new_stones.append(int(second_half))
        else:
            new_stones.append(2024 * stone)
    return new_stones


stones = [int(stone) for stone in input().split()]

for _ in range(25):
    stones = blink_transform(stones)

print(len(stones))
