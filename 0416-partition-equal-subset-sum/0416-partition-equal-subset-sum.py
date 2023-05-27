class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def dp(i,target):
            if target == 0: return True
            if i >= len(nums): return False
            return dp(i+1,target-nums[i]) or dp(i+1,target)
        
        return sum(nums) % 2 == 0 and dp(0,sum(nums)//2)