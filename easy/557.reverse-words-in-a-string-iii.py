class Solution:
    
    def reverse(self, s: List) -> str:
        i,j = 0, len(s)-1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return ''.join(s)
    
    def reverseWords(self, s: str) -> str:
        w_b = 0
        res = []
        for w_e in range(len(s)):
            if s[w_e] == " ":
                res.append(self.reverse(list(s[w_b: w_e])))
                w_b = w_e + 1
        if w_b <= w_e:
            res.append(self.reverse(list(s[w_b: w_e+1])))
                
        return " ".join(res)
                
            
        