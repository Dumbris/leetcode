class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        types = set(candyType)
        _max = len(candyType) / 2
        return min(int(_max), len(types))
        