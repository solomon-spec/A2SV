class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            if nums[i] != i +1 and nums[nums[i] - 1] != nums[i]:
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
            else:
                i += 1

        ans = []
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                ans.append(nums[i])

        return ans