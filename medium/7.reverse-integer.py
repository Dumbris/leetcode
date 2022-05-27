class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        m = 1
        if x < 0:
            m = -1
            
        res = int((str(x*m)[::-1])) * m
        if(abs(res) > (2 ** 31 - 1)):
            return 0
        return res