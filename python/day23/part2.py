from collections import defaultdict


adjacency_map = defaultdict(set)

while True:
    try:
        line = input()
        computers = line.split("-")
        [first, second] = computers

        adjacency_map[first].add(second)
        adjacency_map[second].add(first)
    except EOFError:
        break

cliques = []


# https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm
# this finds all maximal cliques in an undirected graph
# current_clique (R): initially empty, stores current clique
# to_search (P): initially the set of all vertices
# X: initially empty, set of vertices not in P that could form a clique when added to R
def bron_kerbosch(current_clique, to_search, X):
    if len(to_search) == 0 and len(X) == 0:
        # no more vertices to add, R is maximal
        cliques.append(current_clique)
        return

    while to_search:
        vertex = to_search.pop()
        bron_kerbosch(
            current_clique.union({vertex}),
            to_search.intersection(adjacency_map[vertex]),
            X.intersection(adjacency_map[vertex]),
        )

        X = X.union({vertex})


bron_kerbosch(set(), set(adjacency_map.keys()), set())

largest_clique = max(cliques, key=len)
print(",".join(sorted(list(largest_clique))))
