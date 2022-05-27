import math
import operator

class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        s = math.inf
        ans = []
        for i, val1 in enumerate(list1):
            for j, val2 in enumerate(list2):
                if val1 == val2:
                    if i + j == s:
                        ans.append(val1)
                    elif (i + j) < s:
                        s = i + j
                        ans = [val1]
                    
        #return [char[1] for char in sorted(ans, key=operator.itemgetter(0))]
        return ans

#["Shogun","Tapioca Express","Burger King","KFC"]
#["KFC","Burger King","Tapioca Express","Shogun"]