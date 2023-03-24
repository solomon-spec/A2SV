class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.append(-1)
        i = 0 
        while i < len(nums):
            if nums[i] != i and nums[i] != -1:
                nums[nums[i]],nums[i] = nums[i],nums[nums[i]]
            else:
                i += 1

        
        for i in range(len(nums)):
            if i != nums[i]:
                return i
            
        return len(nums)