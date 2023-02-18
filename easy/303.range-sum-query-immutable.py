class NumArray:

    def __init__(self, nums: List[int]):
        cumsum = 0
        self.cumarr = []
        for n in nums:
            cumsum += n
            self.cumarr.append(cumsum)
            

    def sumRange(self, left: int, right: int) -> int:
        left_sum = self.cumarr[left-1] if left > 0 else 0
        return self.cumarr[right] - left_sum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)