import math
class Solution:
    def get_i(self, x, i):
        return int(x/math.pow(10,i)) - int(x/math.pow(10,i+1))*10
    
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True 
        
        if x < 0:
            return False
        
        #x = abs(x)
        
        
        
        l = int(math.log10(x))+1
        
        #print(l)
        
        if l == 1:
            return True 
        
        for i1 in range(l//2+1):
            i2 = l-1-i1
            d1 = self.get_i(x, i1)
            d2 = self.get_i(x, i2)
            #print(i1, d1, i2, d2)
            if d1 != d2:
                return False
        return True
            
        