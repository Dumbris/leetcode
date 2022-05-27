class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        costs = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
        
        left = 0
        max_res = 0
        cur_sum = 0
        for right in range(len(costs)):
            cur_sum += costs[right]
            while cur_sum > maxCost:
                cur_sum -= costs[left]
                left += 1
            max_res = max(max_res, right - left + 1)
        
        return max_res