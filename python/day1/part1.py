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

sums = 0
for i in range(len(l1)):
    difference = abs(l1[i] - l2[i])
    sums += difference

print(sums)
