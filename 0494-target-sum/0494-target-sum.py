class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = defaultdict(int)
        def dp(i,tar):
            if i == len(nums):
                if tar == target: return 1
                return 0
            state = (i,tar)
            
            if state not in memo:
                memo[state] = dp(i+1,tar-nums[i]) + dp(i+1,tar+nums[i])
            return memo[state]
        return dp(0,0)