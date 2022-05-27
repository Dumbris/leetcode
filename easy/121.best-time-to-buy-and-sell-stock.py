class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        
        max_ = 0
        min_ = prices[0]
        for i, curr in enumerate(prices):
            if curr < min_:
                min_ = curr
            elif curr - min_ > max_:
                max_ = curr - min_    
                
        return max_