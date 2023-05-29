class Solution:
    def rob(self, nums: List[int]) -> int:
        arr = [-1]*len(nums)
        if len(nums) == 1: return nums[0]
        def dp(start,end):
            if end < start: return 0
            if start == end:return nums[start]
            print(start,end)
            if arr[end] == -1:
                arr[end] = max(dp(start,end-1),dp(start,end-2)+nums[end])
            return arr[end]
        ans =dp(1,len(nums)-1)
        arr = [-1]*len(nums)
        ans = max(ans,dp(0,len(nums)-2))
        return ans
        