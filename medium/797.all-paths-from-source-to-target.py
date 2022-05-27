from collections import deque

class Vertex:
    def __init__(self, _id, parent=None):
        self.id = _id
        self.parent = parent
        
def to_arr(vertex, res=[]):
    if vertex.id == 0:
        res.append(vertex.id)
        return res
    if vertex.parent:
        to_arr(vertex.parent, res)
    res.append(vertex.id)    
    return res

def to_arr2(vertex):
    res = [vertex.id]
    next_ = vertex.parent
    while next_:
        res.append(next_.id)
        if next_.id == 0:
            return res
        next_ = next_.parent
    return res
    
        

class Solution:
    def neighbors(self, graph, v):
        res = []
        for edge in graph[v.id]:
            res.append(Vertex(edge,v))
        return res
    
    def bfs(self, graph, s, f):
        start = Vertex(s)
        q = deque([start])
        res = []
        visited = set()
        while q:
            vertex = q.pop()
            #print(vertex.id)
            if vertex.id == f:
                res.append(vertex)
            
            if vertex not in visited:
                for neighbor in self.neighbors(graph, vertex):
                    if neighbor not in visited:
                        q.append(neighbor)
                visited.add(vertex)
        return res
            
        
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        #graph[i] is a list of all nodes j for which the edge (i, j) exists.
        #[[1,2], [3], [3], []]
        s = 0
        f = len(graph) - 1
        return [to_arr2(v)[::-1] for v in self.bfs(graph, s, f)]
            
        