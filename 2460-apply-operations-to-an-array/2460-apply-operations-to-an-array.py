class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i]*=2
                nums[i+1] = 0
        
        pointer1 = 0
        
        for i in range (len(nums)):
            if nums[i] != 0 :
                nums[i],nums[pointer1] = nums[pointer1], nums[i]
                pointer1 +=1
                
        return nums