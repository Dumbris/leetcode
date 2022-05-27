"""
abcab*cbb^


pw*wke^w
"""
#abc

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        right = 0
        dist_max = 0
        while right < len(s):
            char = s[right]
            if char in seen:
                seen.remove(s[left])
                left += 1
            else:
                seen.add(char)
                right += 1
            #print(seen)
            dist_max = max(right - left, dist_max)
        return dist_max
            