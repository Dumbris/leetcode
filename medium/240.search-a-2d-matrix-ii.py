import bisect

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R = len(matrix)
        C = len(matrix[0])
        for row in range(R):
            #print(matrix[row])
            if matrix[row][0] <= target and matrix[row][C-1] >= target:
                
                i = bisect.bisect_left(matrix[row], target)
                #print(i)
                if i != len(matrix[row]) and matrix[row][i] == target:
                    return True
        return False