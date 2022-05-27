"""
[0,1,2,2]
   ^   ^
 
 0-1,1-1;
 1-1,2-1;
 1-1,2-2;
"""


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq = {}
        res = 0
        startWindow = 0
        for endWindow in range(len(fruits)): #3
            f_right = fruits[endWindow] #f_r = 2
            if f_right not in freq:
                freq[f_right] = 0
            freq[f_right] += 1 #1:1, 2:2
            while len(freq) > 2:
                f_left = fruits[startWindow] #0
                freq[f_left] -= 1
                if freq[f_left] == 0:
                    del freq[f_left] #1:1, 2:1
                startWindow += 1
            res = max(res, endWindow - startWindow + 1) #2 3-1+1
        return res
        