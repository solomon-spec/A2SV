class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        summ = sum(nums)
        cur = 0
        for i in range(len(nums)):
            if cur == summ - cur - nums[i]:
                return i
            cur += nums[i]
        return -1
             
            
        
    