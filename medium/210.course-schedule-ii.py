from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses)}
        inEdges = {i:0 for i in range(numCourses)}
        
        for child,parent in prerequisites:
            graph[parent].append(child)
            inEdges[child] += 1
        
        sources = deque()
        ordered = []
        
        for i in range(numCourses):
            if inEdges[i] == 0:
                sources.append(i)
                
        while sources:
            vertex = sources.popleft()
            ordered.append(vertex)
            for v in graph[vertex]:
                inEdges[v] -= 1
                if inEdges[v] == 0:
                    sources.append(v)
        return ordered if len(ordered) == numCourses else []
            
        