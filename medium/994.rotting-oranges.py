"""

        r-1,c
r,c-1; r,c; r,c+1
      r+1,c
"""

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def select_cells(grid: List[List[int]], t:int) -> List[int]:
            res = []
            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    #print(r,c)
                    if grid[r][c] == t:
                        res.append((r,c))
            return res
        
        def neibours(grid: List[List[int]], r,c) -> List[int]:
            R = len(grid)
            C = len(grid[0])
            res = []
            if r - 1 < R and r - 1 >= 0:
                res.append((r-1,c))
            if r + 1 < R and r + 1 >= 0:
                res.append((r+1,c))
            if c - 1 < C and c - 1 >= 0:
                res.append((r,c-1))
            if c + 1 < C and c + 1 >= 0:
                res.append((r,c+1))
            #print(res)
            return res
        
        q = deque()
        for item in select_cells(grid,2):
            q.append((0,item))
        max_level = 0
        while len(q) > 0:
            #print(q)
            level, item = q.popleft()
            max_level = max(max_level, level)
            r,c = item
            for nr,nc in neibours(grid, r,c):
                
                if grid[nr][nc] == 1:
                    #print(nr,nc)
                    grid[nr][nc] = 2
                    q.append((level+1, (nr,nc)))
        remains = select_cells(grid,1)
        #print(remains)
        if len(remains) > 0:
            return -1
        return max_level
        