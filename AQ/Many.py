from queue import PriorityQueue

class graph:
  def __init__(self, reds, start, terminal, G):
    self.reds = reds
    self.start = start
    self.terminal = terminal
    self.g = G

def getgraph():
    g = {}
    reds = set()
    nr_verts, nr_edges, nr_reds = map(int, input().split())
    start, terminal = input().split()
    start = (start, 0)
    terminal = (terminal, 0)
    for _ in range(nr_verts):
        vertin = input().strip()
        if vertin.endswith('*'):
            vertin = vertin[:-1].strip()
            reds.add(vertin)
        g[vertin] = []

    for _ in range(nr_edges):
        vert1, direction, vert2 = input().split()

        if vert1 in reds:
            weight1 = 1
        else:
            weight1 = 0
        if vert2 in reds:
            weight2 = 1
        else:
            weight2 = 0


        g[vert1].append((vert2, weight2))
        if direction == "--":
            g[vert2].append((vert1, weight1))
    return graph(reds,start,terminal,g)

def weighted(G):
    start = G.start[0]

    distance = {v: -1 for v in G.g}  
    distance[start] = 1 if start in G.reds else 0

    queue = PriorityQueue()
    queue.put((-distance[start], start)) 

    while not queue.empty():
        _, u = queue.get()
        for v, w in G.g[u]:
            if distance[u] + w > distance[v]:
                distance[v] = distance[u] + w
                queue.put((-distance[v], v))

    return distance[G.terminal[0]]

G = getgraph()
print(weighted(G))