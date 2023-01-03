class Solution(object):
    def buildArray(self, nums):
        nums2 = []
        for i in nums:
            nums2.append(nums[i])
            
        return nums2
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        