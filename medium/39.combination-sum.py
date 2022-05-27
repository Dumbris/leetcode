class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        def combi(fixed: List[int], remind: int):
            if remind == 0:
                fixed.sort()
                fixed = tuple(fixed)
                if fixed not in res:
                    res.add(fixed)
            if remind > 0:    
                for i in candidates:
                    combi(fixed + [i], remind - i)
                
        combi([], target)
        
        return res