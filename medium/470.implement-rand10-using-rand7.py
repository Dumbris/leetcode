# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        r = 100
        while True:
            r = 7*(rand7()-1) + rand7()
            if r <= 40:
                break
            
        return 1 + r % 10