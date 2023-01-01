class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pt1 = 0
        for pt2 in range(len(nums)):
            if nums[pt2] == 0:
                continue
            else:
                nums[pt1] = nums[pt2]
                pt1+=1
        
        while pt1<len(nums):
            nums[pt1]=0
            pt1+=1