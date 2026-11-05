from collections import deque


class graph:
  def __init__(self, reds, start, terminal, G):
    self.reds = reds
    self.start = start
    self.terminal = terminal
    self.G = G

def getgraph():
    G = {}
    reds = set()
    nr_verts, nr_edges, nr_reds = map(int, input().split())
    start, terminal = input().split()
    for _ in range(nr_verts):
        vertin = input().strip()
        if vertin.endswith('*'):
            vertin = vertin[:-1].strip()
            reds.add(vertin)
        G[vertin] = []

    for _ in range(nr_edges):
        vert1, direction, vert2 = input().split()
        G[vert1].append(vert2)
        if direction == "--":
            G[vert2].append(vert1)
    return graph(reds,start,terminal,G)

G = getgraph()

def bfs(G):
    visited = set()
    start = G.start

    if G.start in G.reds:
        return -1
    
    queue = deque([start])
    distance = {start: 0}
    visited.add(start)
    
    while queue:
        start = queue.popleft()
        if start == G.terminal:
            return distance[start]
        for v in G.G[start]:
            if v in visited:
                continue
            if v not in G.reds:
                visited.add(v)
                distance[v] = distance[start] + 1
                queue.append(v)
    return -1

print(bfs(G))