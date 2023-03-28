class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != i + 1 and nums[nums[i] - 1] != nums[i] :
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
            else:
                i += 1

        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i + 1
        return len(nums)  + 1  