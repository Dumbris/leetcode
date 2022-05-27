# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        i,j = 1,n
        while i < j:
            m = i + ((j-i) // 2)
            if isBadVersion(m):
                #left
                j = m
            else:
                #right
                i = m+1
        return i
        """
        1*,2*,3*,4*,5
        """