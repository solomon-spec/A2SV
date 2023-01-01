class Solution(object):
    def removeElement(self, nums, val):
        total = len(nums)
        i=0
        while i in range(len(nums)):
            if nums[i] == val:
                nums.pop(i)
                nums.append("_")
                total-=1
            else:
                i+=1
        return total
                
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        