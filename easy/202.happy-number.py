class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            i, r = divmod(n, 10)
            n = r**2
            while i > 0:
                i, r = divmod(i, 10)
                n += r**2
        return True
        