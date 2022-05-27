class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self._search(nums,target, 0)
    
    def _search(self, nums: List[int], target: int, shift:int) -> int:
        #print(nums)
        if len(nums) == 1:
            if nums[0] == target:
                return shift
            else:
                return -1
        
        l = len(nums) // 2
        if nums[l] == target:
            return shift+l
        elif nums[l] < target:
            #target in right part
            return self._search(nums[l:], target, l+shift)
        else:
            return self._search(nums[:l], target, shift)