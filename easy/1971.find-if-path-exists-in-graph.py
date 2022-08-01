from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        edges2 = defaultdict(list)
        for e in edges:
            u, v = e
            edges2[u].append(v)
            edges2[v].append(u)
        seen = set()
        def dfs(node):
            if node == destination:
                return True
            if node not in edges2:
                return False
            for e in edges2[node]:
                if e not in seen:
                    seen.add(e)
                    if dfs(e):
                        return True
                    
            return False
        #print(edges2)
        return dfs(source)
            
        