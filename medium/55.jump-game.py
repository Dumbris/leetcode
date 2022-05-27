class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if [0] == nums:
            return True
        
        li = len(nums)-1
        curr_pos = 0
        while nums[curr_pos] > 0:
            
            if (nums[curr_pos] + curr_pos) >= li:
                return True
            
            #choose curr_pos
            max_ = -1
            max_pos = -1
            for n in range(1, nums[curr_pos]+1):
                m_ = nums[curr_pos+n] - (nums[curr_pos] - n)
                #print(max_, m_)
                if (m_) > max_:
                    max_ = m_
                    max_pos = curr_pos+n
            
            curr_pos = max_pos if max_pos > 0 else curr_pos
            #print("C ->",curr_pos)
            
            
            
        return False
            