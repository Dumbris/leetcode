class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.image = image
        self.seen = set()
        self.newColor = newColor
        self.oldColor = image[sr][sc]
        self.n = len(image) #2 num rows
        self.m = len(image[0]) #3 num cols
        self._floodFill(sr,sc)
        return self.image
    
    def _floodFill(self, sr: int, sc: int) -> None:
        if sr >= self.n or sc >= self.m or sr < 0 or sc < 0:
            return
        
        if (sr,sc) in self.seen:
            return
        
        self.seen.add((sr,sc))
        
        if self.oldColor != self.image[sr][sc]:
            return
        
        self.image[sr][sc] = self.newColor
        
        
        self._floodFill(sr-1,sc)
        self._floodFill(sr+1,sc)
        self._floodFill(sr,sc-1)
        self._floodFill(sr,sc+1)