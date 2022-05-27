class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        _j = set(J)
        counter = 0
        for s in S:
            if s in _j:
                counter += 1
        return counter
        
        