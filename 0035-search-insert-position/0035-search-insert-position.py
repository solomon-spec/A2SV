class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) -1 
        
        if nums[end]<target:
            return end + 1
        
        while start <= end:
            
            middle = (start+end)//2
            
            if nums[middle] == target:
                return middle
            
            if nums[middle] > target:
                end = middle - 1
                
            else:
                start = middle + 1
        
        if nums[middle] < target:
            return middle +1
        else:
            return middle