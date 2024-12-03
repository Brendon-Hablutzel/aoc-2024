l1 = []
l2 = []

while True:
    try:
        line = input()
    except EOFError:
        break

    [num1, num2] = [int(n) for n in line.split()]
    l1.append(num1)
    l2.append(num2)

l1.sort()
l2.sort()

similarity = 0

for element in l1:
    freq = l2.count(element)
    score = element * freq
    similarity += score

print(similarity)
