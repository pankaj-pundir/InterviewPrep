from graph_data import GraphData
import heapq

class ShortestPath:
    def __init__(self,gd):
        self.graph_data:GraphData = gd
        self.data = gd.data

    def dijkstra(self,src,dst):
        heap = []
        visited = [ False for _ in range(self.graph_data.vertices)]
        value = [ float("inf") for _ in range(self.graph_data.vertices)]
        parent = [ -1 for _ in range(self.graph_data.vertices)]

        heapq.heappush(heap,src)
        value[src] = 0

        while len(heap) > 0:
            node = heapq.heappop(heap)
            visited[node] = True
            for _n in self.data[node]:
                if self.graph_data.get_wt(node,_n) + value[node] < value[_n] and visited[_n] == False:
                    value[_n] =  self.graph_data.get_wt(node,_n) + value[node]
                    heapq.heappush(heap,_n)
                    parent[_n] = node
        # print path
        _n = dst
        path = []
        while src != _n:
            path.append(_n)
            _n = parent[_n]
        path.append(_n)

        return " -> ".join(list(map(str,path[::-1])))

    
gd = GraphData(6,"undirected","adj_list")
gd.add_edge(0,2,3)
gd.add_edge(0,1,4)
gd.add_edge(1,2,1)
gd.add_edge(1,3,4)
gd.add_edge(2,3,2)
gd.add_edge(3,4,5)
gd.add_edge(2,4,2)
gd.add_edge(4,5,6)
gd.add_edge(3,5,7)

sp = ShortestPath(gd)
print("============== DIJKSTRA ==================")
print(sp.dijkstra(1,3))