class DisjointSet:
    def __init__(self,size ) -> None:
        self._size = size

        self.parent = [-1 for i in range(size)]
        self.rank = [0 for i in range(size)]

    def findParent(self,val): # path compression approach
        if self.parent[val] == -1:
            return val
        self.parent[val] = self.findParent(self.parent[val])
        return self.parent[val]
    
    def union(self,val1, val2): # path compression approach
        parent1 = self.findParent(val1)
        parent2 = self.findParent(val2)

        if parent1 == parent2:
            return
        
        if self.rank[parent1] < self.rank[parent2]:
            self.parent[parent1] = parent2
        elif self.rank[parent1] > self.rank[parent2]:
            self.parent[parent2] = parent1
        else:
            self.parent[parent2] = parent1
            self.rank[parent2] +=1
        
    def is_same_set(self,a,b):
        if self.findParent(a) == self.findParent(b):
            return True
        return False

    
# dsuf = DisjointSet(5)
# dsuf.union(1,2)
# dsuf.union(1,3)
# dsuf.union(0,4)
# dsuf.union(2,4)
# print(dsuf.parent)
# print(dsuf.is_same_set(4,2))