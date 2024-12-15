m = []


while True:
    try:
        line = input()
    except EOFError:
        break

    [total, numbers] = line.split(": ")

    m.append((int(total), [int(d) for d in numbers.split()]))


def is_valid(target, nums):
    def track(sum_so_far, nums_remaining):
        if len(nums_remaining) == 0:
            return sum_so_far == target

        next_num = nums_remaining.pop(0)

        new_nums1 = nums_remaining.copy()
        res1 = track(sum_so_far + next_num, new_nums1)

        new_nums2 = nums_remaining.copy()
        res2 = track(sum_so_far * next_num, new_nums2)

        new_nums3 = nums_remaining.copy()
        res3 = track(int(str(sum_so_far) + str(next_num)), new_nums3)

        return res1 or res2 or res3

    return track(0, nums)


summed = 0
for total, nums in m:
    if is_valid(total, nums):
        summed += total

print(summed)
