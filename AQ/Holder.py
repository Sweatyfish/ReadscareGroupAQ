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
        vertin = input()
        if vertin.endswith('*'):
            vertin = vertin[:-1].strip()
            reds.add(vertin)
        G[vertin] = []
    for _ in range(nr_edges):
        vert1,_,vert2 = input().split()
        vert1.strip()
        vert2.strip()
        G[vert1].append(vert2)
    g = graph(reds,start,terminal,G)
    return g



print(getgraph())