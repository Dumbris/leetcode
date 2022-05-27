"""
(0,0)(0,1)(0,2)(0,3)
(1,0)(1,1)(1,2)(1,3)
(2,0)(2,1)(2,2)(2,3)
"""

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        R = len(matrix)
        C = len(matrix[0])
        for c in range(C):
            i = 0
            n = matrix[i][c]
            while c+i<C and i<R:
                if n != matrix[i][c+i]:
                    return False        
                i += 1
        for r in range(1,R):
            i = 0
            n = matrix[r][i]
            while i<C and r+i<R:
                if n != matrix[r+i][i]:
                    return False        
                i += 1
        return True
            
        