class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        h = {}
        h[0] = -1
        cur_sum = 0
        res = 0
        for i,v in enumerate(nums):
            if v == 0:
                cur_sum -= 1
            else:
                cur_sum += 1
            if cur_sum not in h:
                h[cur_sum] = i
            else:
                res = max(i - h[cur_sum], res)
        #print(h)
        if cur_sum == 0:
            return len(nums)

        return res

"""
[0,1,0,1,0,1]

[1,1,2,2,3,3]
[0,1,1,2,2,3]

[0,1,0]
1,1,2
0,1,1

0,0,1,1,0,0
1,2,2,2,3,4
0,0,1,2,2,3

1,0,1,0,0,1,0,1,1
0,1,1,2,3,3,4,4,4
1,1,2,2,2,3,3,4,5

0,0,0,0,1
-1,-2,-3,-4,-3

1,2,3,4,4
0,

"""