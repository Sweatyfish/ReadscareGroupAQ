



def getgraph():
    G = {}
    reds = set()
    nr_verts,nr_edges,nr_reds = map(int, input().split())
    start,terminal = input().split()
    
    for i in range(nr_verts):
        vertin = input()
        if vertin.endswith('*'):
            vertin = vertin[:-1].strip()
            reds.add(vertin)
        G[vertin] = []
    for i in range(nr_edges):
        vert1,_,vert2 = input().split()
        vert1.strip()
        vert2.strip()
        print(vert1, "1 ----- 2", vert2)
        G[vert1].append(vert2)
    return G,reds




print(getgraph())


