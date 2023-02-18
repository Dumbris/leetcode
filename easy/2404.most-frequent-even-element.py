from collections import defaultdict
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        h = defaultdict(int)
        for num in nums:
            if num % 2 == 0:
                h[num] += 1
        print(h)
        _max = -math.inf
        _max_value = -1
        for value, count in h.items():
            if (count > _max) or (count == _max and value < _max_value):
                _max = count
                _max_value = value
        return _max_value
