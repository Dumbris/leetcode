from collections import defaultdict, deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = defaultdict(int)
        seen = set()
        q = deque()
        for node1 in range(len(graph)):
            if node1 in seen:
                continue
            color[node1] = 1
            parent_color = 1
            q.extend([n for n in graph[node1] if n not in seen])
            seen.add(node1)
            while q:
                l = len(q)
                for _ in range(l):
                    node = q.popleft()
                    must_color = parent_color * -1 #invert color
                    if color[node] == 0:
                        color[node] = must_color
                        seen.add(node)
                    elif color[node] != must_color:
                        #print(node, graph[node], q, color[node], must_color)
                        return False
                    q.extend([n for n in graph[node] if n not in seen])
                parent_color = parent_color * -1 #invert color
        return True
        