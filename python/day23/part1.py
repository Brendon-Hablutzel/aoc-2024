from itertools import combinations
from collections import defaultdict

computers = set()

connections = defaultdict(set)

while True:
    try:
        line = input()
        conn_computers = line.split("-")
        [first, second] = conn_computers
        computers.add(first)
        computers.add(second)

        connections[first].add(second)
        connections[second].add(first)
    except EOFError:
        break


def is_valid_connection(conn_computers):
    a, b, c = conn_computers
    a_conns = connections[a]
    b_conns = connections[b]
    c_conns = connections[c]

    group = {a, b, c}

    return (
        len(group.intersection(a_conns)) == 2
        and len(group.intersection(b_conns)) == 2
        and len(group.intersection(c_conns)) == 2
    ) and (a.startswith("t") or b.startswith("t") or c.startswith("t"))


num_valid_connections = [
    is_valid_connection(comb) for comb in combinations(computers, 3)
].count(True)

print(num_valid_connections)
