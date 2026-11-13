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
    visited.add(start)
    
    while queue:
        start = queue.popleft()
        colour = start in G.reds
        if start == G.terminal:
            return True
        for v in G.G[start]:
            if v in visited:
                continue
            if colour != (v in G.reds):
                visited.add(v)
                queue.append(v)
    return False
print(bfs(G))

