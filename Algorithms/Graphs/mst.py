from graph_data import GraphData
from disjoint_set import DisjointSet

class Mst:
    def __init__(self,gd):
        self.graph_data:GraphData = gd
        self.data = gd.data
    
    def krushkal(self,):
        dsuf = DisjointSet(self.graph_data.vertices)

        _data = sorted(self.data,key = lambda x:x[2])
        edge_data = []
        sum_w = 0
        for v1,v2,w in _data:
            if dsuf.is_same_set(v1,v2):
                continue
            sum_w += w
            edge_data.append((v1,v2,w))
            dsuf.union(v1,v2)
        return edge_data




gd = GraphData(6,"undirected","edge_list")
gd.add_edge(0,2,3)
gd.add_edge(0,1,4)
gd.add_edge(1,2,1)
gd.add_edge(1,3,3)
gd.add_edge(2,3,2)
gd.add_edge(3,4,5)
gd.add_edge(2,4,2)
gd.add_edge(4,5,6)
gd.add_edge(3,5,7)

mst = Mst(gd)
print("\n============= KRUSHKAL ===================")
print(mst.krushkal())
