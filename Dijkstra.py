

import heapq

def dj(g, s):
    d = {x: float('inf') for x in g}
    d[s] = 0
    q = [(0, s)]

    while q:
        c, u = heapq.heappop(q)
        for v, w in g[u]:
            if d[u] + w < d[v]:
                d[v] = d[u] + w
                heapq.heappush(q, (d[v], v))
    return d

g = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

s = 'A'
r = dj(g, s)

print(f"From {s}:")
for x in r:
    print(f"{s} -> {x} = {r[x]}")


