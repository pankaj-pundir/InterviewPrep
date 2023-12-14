from graph_data import GraphData

class GraphTraversal:
    def __init__(self,data):
        self.graph_data: GraphData = data
        self.data = data.data
        self.traversed_path = []

    def init_dfs(self,init_node = 0):
        # default option is adj list.
        if not self.graph_data.match_data_store_type_and_edge_catgory(edge_category="undirected",data_store_type = "adj_list"):
            raise RuntimeError("Graph category not supported for DFS")
        
        visited = [False for _ in range(self.graph_data.vertices)]
        traversed_path = []

        def dfs(node):
            if visited[node]:
                return
            visited[node] = True
            traversed_path.append(node)
            for _node in self.data[node]:
                dfs(_node)

        dfs(init_node)
        self.traversed_path = traversed_path
    
    def init_bfs(self,init_node = 0):
        # default option is adj list.
        if not self.graph_data.match_data_store_type_and_edge_catgory(edge_category="undirected",data_store_type = "adj_list"):
            raise RuntimeError("Graph category not supported for BFS")
        
        visited = [False for _ in range(self.graph_data.vertices)]
        traversed_path = []
        queue = Queue()
        queue.put(init_node)

        while not queue.empty():

            node_id = queue.get()
            if visited[node_id] == True:
                # queue.get()
                continue

            visited[node_id] = True
            traversed_path.append(node_id)
            for _ in self.data[node_id]:
                if visited[_] == False:
                    queue.put(_)
        self.traversed_path = traversed_path
    
    def show_path(self):
        print("============= PATH ===================")
        print(self.traversed_path)

class AdvGraph(GraphTraversal):
    def __init__(self,gd) -> None:
        super().__init__(gd)
        
    def topological_sort(self):
        # Khan's algorithm
        indegree = [0 for i in range(self.graph_data.vertices)]

        q = Queue()
        # count indegree
        for node in self.data:
            for nn in node:
                indegree[nn] +=1
            
        for ind,in_degre in enumerate(indegree):
            if in_degre == 0:
                q.put(ind)

        sorted_array = []
        while not q.empty():
            ind =  q.get()
            sorted_array.append(ind)

            for rm_node in self.data[ind]:
                indegree[rm_node] -=1
                if indegree[rm_node] == 0:
                    q.put(rm_node)
        if len(sorted_array) != self.graph_data.vertices:
            print("Its not a DAG")
            return None
        return sorted_array



    def init_articulation_point(self):

        discovery_time = [-1 for _ in range(self.graph_data.vertices)]
        low_time = [-1 for _ in range(self.graph_data.vertices)]
        parent_node = [-1 for _ in range(self.graph_data.vertices)]
        ap = [False for _ in range(self.graph_data.vertices)]
        counter = 0 # time counter.

        def ap_dfs(node):
            nonlocal counter

            discovery_time[node] = low_time[node] = counter
            counter += 1 
            children = 0
            # print(f"current node {node} counter {counter}")
            for _node in self.data[node]:
                if discovery_time[_node ] == -1: # not visited.
                    children +=1
                    parent_node[_node] = node
                    ap_dfs(_node)
                    low_time[node] = min(low_time[node],low_time[_node]) # update low time

                    if parent_node[node] == -1 and children > 1: # root node check
                        ap[node] = True
                    
                    if parent_node[node] != -1 and low_time[_node] >= discovery_time[node]:
                        ap[node] = True

                else:
                    low_time[node] = min(low_time[node],discovery_time[_node]) # back edge.

        for ini_node in range(self.graph_data.vertices):
            if discovery_time[ini_node] == -1:
                ap_dfs(ini_node)

        # print(discovery_time)
        # print(low_time)
        # print(parent_node)
        return ap



# Input data 
# gd = GraphData(6,"undirected","adj_list")
# gd.add_edge(1,2)
# gd.add_edge(2,3)
# gd.add_edge(2,4)
# gd.add_edge(4,5)
# gd.add_edge(5,0)
# gd.add_edge(4,0)

# gd.show()

# gt = GraphTraversal(gd)
# gt.init_bfs(0)
# gt.show_path()

# advance graph

gd = GraphData(6,"directed","adj_list")
gd.add_edge(0,2)
gd.add_edge(0,3)
gd.add_edge(0,1)
gd.add_edge(1,2)
gd.add_edge(4,3)
gd.add_edge(5,3)
# gd.add_edge(4,0)

ag = AdvGraph(gd)
print("=============ARTICULATION POINT===================")
print(ag.init_articulation_point())


gd = GraphData(5,"directed","adj_list")
gd.add_edge(0,1)
gd.add_edge(1,2)
gd.add_edge(1,3)
gd.add_edge(2,4)
gd.add_edge(4,3)
gd.add_edge(3,2)
ag = AdvGraph(gd)
print("=============TOPOLOGICAL SORT===================")
print(ag.topological_sort())