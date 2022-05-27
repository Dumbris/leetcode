"""
ADOBECODEBANC
 ^   ^



A:1,B:0,C:1, match = 1

A:1,B:1,C:1

"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        startWindow = 0
        res = ""
        freq = {}
        match = 0
        #build etalon
        for ch in t:
            if ch not in freq:
                freq[ch] = 1
            else:
                freq[ch] += 1
        #A:1,B:1,C:1                
        for endWindow in range(len(s)): #ADOBECODEBANC
            ch_right = s[endWindow] #B
            #add char
            if ch_right in freq:
                freq[ch_right] -= 1 #A:0,B:0,C:0
                if freq[ch_right] >= 0:
                    match += 1 #2
            #print(freq, s[startWindow:endWindow+1], match)
                
            while match >= len(t): #5>3
                
                ch_left = s[startWindow]
                
                #remove char
                if ch_left in freq:
                    freq[ch_left] += 1 ##A:1,B:0,C:0
                    if freq[ch_left] > 0:
                        match -= 1
                #print("while", freq, ch_left, s[startWindow:endWindow+1], match)
                if (len(res) == 0) or (len(s[startWindow:endWindow+1]) < len(res)):
                    res = s[startWindow:endWindow+1] #0:5 ADOBEC

                startWindow += 1
        return res
                
