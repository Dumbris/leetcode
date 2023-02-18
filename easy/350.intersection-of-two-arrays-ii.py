class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums1.sort()
        nums2.sort()
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        i,j = 0,0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums2[j])
                j += 1
                i += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return res