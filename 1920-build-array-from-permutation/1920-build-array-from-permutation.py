class Solution(object):
    def buildArray(self, nums):
        nums2 = [0 for i in nums]
        for i in range(len(nums)):
            nums2[i] = nums[nums[i]]
            
        return nums2
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        