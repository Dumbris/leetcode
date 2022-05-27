class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        types = set()
        n = len(candyType) / 2
        for t in candyType:
            if t not in types and len(types) < n:
                types.add(t)
            if len(types) >= n:
                return len(types)
        return len(types)
                
        