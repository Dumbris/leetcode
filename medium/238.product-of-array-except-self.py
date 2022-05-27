class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        prod = 1
        for i in nums:
            prod *= i
            prefix.append(prod)

        sufix = []
        prod = 1
        for i in range(len(nums)-1,-1,-1):
            prod *= nums[i]
            sufix.append(prod)
        sufix.reverse()
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(sufix[i+1])
            elif i == len(nums) - 1:
                res.append(prefix[i-1])
            else:
                res.append(sufix[i+1]*prefix[i-1])

        return res
        