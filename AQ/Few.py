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
    visited = set()
    start = G.start

    queue = PriorityQueue()
    queue.put((0,start))

    startweight = 0
    if start[0] in G.reds:
        startweight = 1
    distance = {start: startweight}
    visited.add(start)
    
    while not queue.empty():
        _, start = queue.get()
        # print("start point", start[0], "terminal", G.terminal[0])
        if start[0] == G.terminal[0]:
            return distance[start]
        for v in G.g[start[0]]:
            if v in visited:
                continue
            visited.add(v)
            distance[v] = distance[start] + v[1]
            # print(v[0], "has a weight of", v[1], "and the distnce is", distance[v])
            queue.put((distance[v], v))

    return -1

G = getgraph()
print(weighted(G))