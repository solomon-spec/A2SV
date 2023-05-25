class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        best = -inf
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            best = max(best,ceil(cur_sum/(i+1)))
        return best