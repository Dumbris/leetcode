class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        longest = 0
        startWindow = 0
        freq = {}
        for endWindow in range(len(s)):
            ch_right = s[endWindow]
            if ch_right not in freq:
                freq[ch_right] = 0
            freq[ch_right] += 1
            while len(freq) > k:
                ch_left = s[startWindow]
                freq[ch_left] -= 1
                if freq[ch_left] == 0:
                    del freq[ch_left]
                startWindow += 1
            longest = max(longest, endWindow - startWindow + 1)
        return longest
        