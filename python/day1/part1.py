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

lists = zip(sorted(l1), sorted(l2))

sums = sum(abs(a - b) for (a, b) in lists)

print(sums)
