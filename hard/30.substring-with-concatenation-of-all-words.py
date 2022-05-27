"""
qbarfoothefoobarman
 ^ ^

bar
"""

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        startWindow = 0
        freq_ = {}
        l = len(words[0])
        for w in words:
            if w in freq_:
                freq_[w] += 1
            else:
                freq_[w] = 1
        match = 0
        buffer = []
        i = 0
        while i <= (len(s) - l * len(words)):
            if s[i:i+l] in set(words):
                startWindow = i #1
                freq = freq_.copy()
                match = 0
                for startWindow in range(i,len(s),l): #1
                    w2 = s[startWindow:startWindow+l] #1:5
                    #print(w2, startWindow, i, freq)
                    if match == len(words):
                        break
                    if w2 in freq:
                        freq[w2] -= 1
                        match += 1
                        if freq[w2] == 0:
                            del freq[w2]
                    else:
                        break
                if match == len(words):
                    res.append(i)
            i += 1
            
        return res



