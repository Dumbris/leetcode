"""
[2,3,4] 6-2=4

[-1,0] -1 - -1 = 0

[-1,0,3] 2 - -1 = 3


[-5,0,3] -2 - -5 = 3

"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = len(numbers)
        last_t = None
        for i in range(0,l):
            _t = target - numbers[i]
            if _t == last_t:
                continue
            for j in range(i+1,l):
                #print(_t, numbers[j], j)
                if numbers[j] == _t:
                    return [i+1,j+1]
            last_t = _t
            
            
            

                