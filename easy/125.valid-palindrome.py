import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s) - 1 
        while l < r:
            if not str.isalnum(s[l]):
                l += 1
                continue
            if not str.isalnum(s[r]):
                r -= 1
                continue
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True
        