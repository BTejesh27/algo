 

import heapq

def ospf(g, src):
    d = {n: float('inf') for n in g}
    d[src] = 0
    q = [(0, src)]
    p = {src: None}

    while q:
        c, u = heapq.heappop(q)
        for v, w in g[u]:
            if d[u] + w < d[v]:
                d[v] = d[u] + w
                p[v] = u
                heapq.heappush(q, (d[v], v))
    return d, p

def show_path(p, dst):
    path = []
    while dst:
        path.append(dst)
        dst = p[dst]
    return ' -> '.join(path[::-1])

g = {
    'R1': [('R2', 2), ('R3', 5)],
    'R2': [('R1', 2), ('R3', 1), ('R4', 3)],
    'R3': [('R1', 5), ('R2', 1), ('R4', 2)],
    'R4': [('R2', 3), ('R3', 2)]
}

src = 'R1'
dist, prev = ospf(g, src)

print(f"OSPF routing from {src}:")
for r in g:
    print(f"{src} → {r}, Cost: {dist[r]}, Path: {show_path(prev, r)}")

