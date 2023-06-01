class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = defaultdict(int)
        def dp(target):
            if target < 0: return 0
            if target == 0: return 1
            if target not in memo:
                for x in nums:
                    memo[target] += dp(target-x)
            return memo[target]
        return dp(target)