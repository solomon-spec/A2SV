class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total_sum = 0
        max_sum = -inf
        for num in nums:
            if total_sum >= 0: total_sum += num
            else: total_sum = num
            max_sum = max(max_sum,total_sum)  
        return max_sum