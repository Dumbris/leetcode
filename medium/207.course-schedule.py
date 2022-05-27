from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inEdges = {i:0 for i in range(numCourses)}
        graph = {i:[] for i in range(numCourses)}
        
        for parent,child in prerequisites:
            graph[parent].append(child)
            inEdges[child] += 1
        
        sources = deque()
        sortedNodes = []
        
        for i in range(numCourses):
            if inEdges[i] == 0:
                sources.append(i)
                
        while sources:
            vertex = sources.popleft()
            sortedNodes.append(vertex)
            for v in graph[vertex]:
                inEdges[v] -= 1
                if inEdges[v] == 0:
                    sources.append(v)
                    
                    
        return len(sortedNodes) == numCourses
        
        
        
        
        