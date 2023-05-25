class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        if len(nums) < 3: return False
        abs_min = nums[0]
        cur_min = inf
        for i in nums:
            if i <= abs_min: abs_min = i
            elif i < cur_min: cur_min = i
            elif abs_min < cur_min < i: return True
        return False

        