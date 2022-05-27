import math
from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        R = len(grid) - 1
        C = len(grid[0]) - 1
        res = math.inf
        seen = set()
        q = deque()
        q.append((0,0,k,0))
        
        while q:
            (r,c,o, steps) = q.popleft()
            if r > R or c > C or r < 0 or c < 0:
                continue
            if grid[r][c] == 1 and o <= 0:
                continue
            if r == R and c == C:
                print(steps)
                return steps
            
            if grid[r][c] == 1 and o > 0:
                o -= 1
            if (r,c,o) in seen:
                continue
            seen.add((r,c,o))
            
            q.append((r+1,c,o,steps+1))
            q.append((r,c+1,o,steps+1))
            q.append((r-1,c,o,steps+1))
            q.append((r,c-1,o,steps+1))
            
        return -1