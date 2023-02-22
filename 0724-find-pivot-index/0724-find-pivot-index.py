class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        summ, cur = sum(nums), 0
        for i, j in enumerate(nums):
            if cur == summ - cur - j:
                return i
            cur += j
        return -1
             
            
        
    