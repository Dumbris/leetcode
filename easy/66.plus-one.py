class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #curry = False
        for i in range(len(digits)-1, -1, -1):
            if digits[i] + 1 < 10:
                digits[i] += 1
                return digits
            else:
                curry = True
                digits[i] = 0
        if curry:
            return [1] + digits
        return digits