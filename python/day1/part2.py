from collections import defaultdict

l1 = []
l2_freq = defaultdict(int)

while True:
    try:
        line = input()
    except EOFError:
        break

    [num1, num2] = [int(n) for n in line.split()]
    l1.append(num1)
    l2_freq[num2] += 1

similarity = sum(element * l2_freq[element] for element in l1)

print(similarity)
