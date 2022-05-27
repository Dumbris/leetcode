class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        startWindow = 0
        freq = {}
        
        
        #calc freq of s1
        freq_s1 = {}
        for ch in s1:
            if ch not in freq_s1:
                freq_s1[ch] = 0
            freq_s1[ch] += 1
            
        def check(freq, freq_s1):
            for k,v in freq_s1.items():
                if (k not in freq) or (v != freq[k]):
                    return False
            return True
            
        for endWindow in range(len(s2)):
            ch_right = s2[endWindow]
            if ch_right not in freq:
                freq[ch_right] = 0
            freq[ch_right] += 1
            
            if (endWindow - startWindow + 1) >= len(s1):
                ch_left = s2[startWindow]
                #check
                if check(freq, freq_s1):
                    return True
                freq[ch_left] -= 1
                if freq[ch_left] == 0:
                    del freq[ch_left]
                startWindow += 1
                
        return False    
        
                
        