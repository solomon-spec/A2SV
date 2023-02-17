class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum=0 #[1,2]
        for i in nums:
            total_sum+=i #28
        left_sum=0 #11
        l=0 #3
        while l<len(nums) and left_sum != total_sum-left_sum-nums[l]: #3<6, 11= 28-11
            if left_sum != total_sum-left_sum-nums[l]:# 
                left_sum+=nums[l] #11
                l+=1
        if l<len(nums) and left_sum == total_sum-left_sum-nums[l]:
            return l 
        else:
            return -1