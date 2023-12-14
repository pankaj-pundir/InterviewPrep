from queue import Queue


class GraphData:
    def __init__(self,vertices,egde_category = "directed",data_store_type = "adj_list"):
        ''' the nodes are 0 indexed, please subtract 1 while adding.'''
        self.data = []
        self.vertices = vertices
        self.__data_store_type = data_store_type
        self.__edge_category = egde_category
        self.init_data(self.__data_store_type)
        self.wt_map = {}

    def match_data_store_type_and_edge_catgory(self,data_store_type,edge_category):
        if self.__data_store_type == data_store_type and self.__edge_category == edge_category:
            return True
        return False
    
    def init_data(self,category = "adj_list"):
        self.__data_store_type = category
        if category == "adj_list":
            self.data = [[] for _ in range(self.vertices)]
        elif category == "adj_matrix":
            self.data = [[0 for i in range(self.vertices)] for _ in range(self.vertices)]
        elif category == "edge_list":
            self.data = []
        else:
            print("Invalid category")
    def add_wt(self,a,b,w):
        self.wt_map[f"{a}_{b}"] = w

    def get_wt(self,a,b):
        return self.wt_map[f"{a}_{b}"]
    
    def add_edge(self,a,b,w = 1):
        if self.__data_store_type is None:
            print("No data store type specified")
            return
        elif self.__data_store_type == "adj_list": 
            self.data[a].append(b)
            if self.__edge_category == "undirected":
                self.data[b].append(a)
                self.add_wt(b,a,w)
            self.add_wt(a,b,w)


        elif self.__data_store_type == "edge_list": 
            self.data.append((a,b,w))

        elif self.__data_store_type == "adj_matrix":
            self.data[a][b] = w
            if self.__edge_category == "undirected":
                self.data[b][a] = w

    def show(self):
        if self.__data_store_type is None:
            print("No data store type specified")
            return
        elif self.__data_store_type == "adj_list": 
            for ind,val in enumerate(self.data):
                print(f"Node {ind} -> {val}")
        elif self.__data_store_type == "adj_matrix":
            for ind,val in enumerate(self.data):
                print(f"Node {ind} -> {val}")
        return
