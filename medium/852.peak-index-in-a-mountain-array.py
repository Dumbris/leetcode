class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        _max = -1
        _i = 0
        #peak_passed = False
        for i, a in enumerate(A):
            #if not peak_passed:
            if a > _max:
                _max = a
                _i = i
        return _i
                
                    