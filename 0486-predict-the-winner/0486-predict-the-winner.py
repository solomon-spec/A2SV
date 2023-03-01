class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dic = {}
        @cache
        def check(start,end):
            if start == end:
                return nums[start]
            return max(nums[start] - check(start+1,end),nums[end] - check(start,end-1))
        return 0<=check(0,len(nums)-1)