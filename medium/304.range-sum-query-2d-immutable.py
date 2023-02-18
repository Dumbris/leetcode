class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.row = len(matrix)
        self.col = len(matrix[0])
        self.sum = [[0] * self.col for _ in range(self.row)]
        for i in range(self.row):
            s = 0
            #print("")
            for j in range(self.col):
                if i > 0:
                    self.sum[i][j] += self.sum[i-1][j]
                if i > 0 and j > 0: 
                    self.sum[i][j] -= self.sum[i-1][j-1]   
                self.sum[i][j] += matrix[i][j] + s
                s = self.sum[i][j]
                #print(str(s)+" ", end='')


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = self.sum[row2][col2]
        if col1-1 >= 0:
            res -= self.sum[row2][col1-1]
        if row1-1 >= 0:
            res -= self.sum[row1-1][col2]
        if col1-1 >= 0 and row1-1 >= 0:
            res += self.sum[row1-1][col1-1]
        return res
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
"""
3 3 4 8 10
8 
"""