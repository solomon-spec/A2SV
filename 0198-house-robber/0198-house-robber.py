class Solution:
    def rob(self, nums: List[int]) -> int:
        arr = [-1]*len(nums)
        def dp(n):
            if n < 0: return 0
            if arr[n] == -1:
                arr[n] = max(dp(n-1),dp(n-2)+nums[n])
            return arr[n]
        return dp(len(nums)-1)