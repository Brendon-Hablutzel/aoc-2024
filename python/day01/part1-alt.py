from heapq import heappush, heappop

l1 = []
l2 = []

n = 0
while True:
    try:
        line = input()
    except EOFError:
        break

    [num1, num2] = [int(n) for n in line.split()]
    heappush(l1, num1)
    heappush(l2, num2)
    n += 1


sums = sum(abs(heappop(l1) - heappop(l2)) for _ in range(n))

print(sums)
