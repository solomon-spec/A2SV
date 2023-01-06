class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        previous_number = nums[0]
        pointer  = 1
        for i in range (1,len(nums)):
            if nums[i] != previous_number:
                nums[pointer] = nums[i]
                pointer+=1
                previous_number = nums[i]
        return pointer
            
                