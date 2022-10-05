class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def r(s, open_count, counter):
            if len(s) == 2*n:
                if open_count == 0:
                    res.append(s)
                return
            
            if open_count < n:
                r(s+"(", open_count+1, counter+1)
            if open_count > 0:
                r(s+")",open_count-1,counter+1)
            
        r("(", 1, 1)
        
        return res