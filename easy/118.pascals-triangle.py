"""
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

[1]
[1,1]
[1,2,1]
[1,3,3,1] 
[1,4,6,4,1]
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res =[[1]]
        for row in range(1,numRows):
            row_res = [1]
            prev_row = res[-1]
            target_len = len(prev_row)
            for i in range(1,target_len+1): #1
                if i < len(prev_row):
                    row_res.append(prev_row[i]+prev_row[i-1])
                #else:
                #    row_res.append(prev_row[i-1])
            res.append(row_res+[1])
            
        return res
        
        