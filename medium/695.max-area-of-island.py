class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.seen = set()
        R = len(grid)
        C = len(grid[0])
        max_area = 0
        self.area = 0
        def dfs(r,c):
            if r >= R or c >= C or r < 0 or c < 0:
                return
            if grid[r][c] == 0:
                return
            if (r,c) in self.seen:
                return
            
            self.area += 1
            self.seen.add((r,c))
            
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
            
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1 and (r,c) not in self.seen:
                    self.area = 0
                    dfs(r,c)
                    #print(self.area)
                    max_area = max(max_area, self.area)
                
        return max_area
        