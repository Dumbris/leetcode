class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def check(s, use_del):
            left, right = 0, len(s) - 1
            while right > left: #0,3; 1,2
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                    continue
                if use_del > 0:
                    use_del -= 1
                    left += 1
                    continue
                return False
            return True
        
        return check(s,1) or check(s[::-1],1)
                    
        