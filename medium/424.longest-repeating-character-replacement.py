"""
A:2
B:1

AABABBA
^ ^ 
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        freq = {}
        startWindow = 0

        def calc_lenght():
            #print(s[startWindow:endWindow], freq)
            return sum(freq.values()) > max(freq.values()) + k
        
        for endWindow in range(len(s)):
            ch_right = s[endWindow]
            if ch_right not in freq:
                freq[ch_right] = 0
            freq[ch_right] += 1
            while calc_lenght():
                ch_left = s[startWindow]
                freq[ch_left] -= 1
                if freq[ch_left] == 0:
                    del freq[ch_left]
                startWindow += 1
            res = max(res, endWindow - startWindow + 1) #2
        
        return res
                
                
        