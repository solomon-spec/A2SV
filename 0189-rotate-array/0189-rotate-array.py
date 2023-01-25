class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        if k == 0 or k == len(nums):
            return nums
        nums1 = nums[-k:]
        nums2 = nums[:-k]
        nums[:k] = nums1
        nums[k:] = nums2